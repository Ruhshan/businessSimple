from django.test import TestCase

from catalogue.models import Product, Price
from operation.models import Receive, DailySummary
from datetime import datetime

class ReceiveTests(TestCase):
    def setUp(self) -> None:
        self.product = Product.objects.create(name="A4 80 GSM")
        self.price = Price.objects.create(product=self.product, buying=5, selling=5, validFrom="2020-08-21", validThrough="2020-12-21")

    def test_receive(self):
        """
            Do: Receive a product A4 80 GSM with Rims per carton: 5, Cartons received: 5, Bonus Units: 0, Date: 21st September, 2020.
            Validate: In stock A4 80 GSM will be 25, in daily summary for 21st September Stock end will be 25.
        """

        receive = Receive.objects.create(product=self.product, price=self.price, date="2020-09-21", unitPerPackage=5,
                                         receivedPackage=5, unit=25)
        date = datetime.strptime("2020-09-21", "%Y-%m-%d")

        stock = DailySummary.objects.get_stock_for_date(date, product=None)
        for l in stock.iterator():
            if l.product == self.product:
                self.assertEqual(l.stockEnd, receive.unit)

        ds = DailySummary.objects.filter(product=self.product, date=date).first()
        self.assertEqual(ds.stockEnd, receive.unit)

    def test_receive_2(self):
        """
            Precondition: Receive a product A4 80 GSM with Rims per carton: 5, Cartons received: 5, Bonus Units: 0, Date: 21st September, 2020.
            Do: Receive a product A4 80 GSM on 14th Semptember 2020, with rimps per carton: 5, carton received: 2, bonus units: 0.
            Validate: In stock A4 80 GSM will be 35 on 21st September.
        """
        Receive.objects.create(product=self.product, price=self.price, date="2020-09-21", unitPerPackage=5,
                               receivedPackage=5, unit=25)

        Receive.objects.create(product=self.product, price=self.price, date="2020-09-14", unitPerPackage=5,
                               receivedPackage=2, unit=10)

        date = datetime.strptime("2020-09-21", "%Y-%m-%d")

        stock = DailySummary.objects.get_stock_for_date(date, product=None)
        for l in stock.iterator():
            if l.product == self.product:
                self.assertEqual(l.stockEnd, 35)

    def test_receive_3(self):
        """
            Pre condition: Execute case 1 and 2
            Do: Receive a product A4 80 GSM on 20th Semptember 2020 with rims per carton 5 and carton received: 5, bonus units: 0.
            Validate: In stock A4 80 GSM will be 60 on 21st September.
        """
        Receive.objects.create(product=self.product, price=self.price, date="2020-09-21", unitPerPackage=5,
                               receivedPackage=5, unit=25)

        Receive.objects.create(product=self.product, price=self.price, date="2020-09-14", unitPerPackage=5,
                               receivedPackage=2, unit=10)

        Receive.objects.create(product=self.product, price=self.price, date="2020-09-20", unitPerPackage=5,
                               receivedPackage=5, unit=25)

        date = datetime.strptime("2020-09-21", "%Y-%m-%d")

        stock = DailySummary.objects.get_stock_for_date(date, product=None)
        for l in stock.iterator():
            if l.product == self.product:
                self.assertEqual(l.stockEnd, 60)


    def test_receive_4(self):
        """
            Precondition : Execute 1 2 3
            Do: Update receive product for A4 80 GSM on 20 th september with rims per carton 5, and carton received: 2 , bonus units: 0
            Validate: In stock A4 80 GSM will be 45 on 21st Septermber.
        """

        Receive.objects.create(product=self.product, price=self.price, date="2020-09-21", unitPerPackage=5,
                               receivedPackage=5, unit=25)

        Receive.objects.create(product=self.product, price=self.price, date="2020-09-14", unitPerPackage=5,
                               receivedPackage=2, unit=10)

        rcv = Receive.objects.create(product=self.product, price=self.price, date="2020-09-20", unitPerPackage=5,
                               receivedPackage=5, unit=25)

        rcv.receivedPackage = 2
        rcv.unit = 10

        rcv.save()

        date = datetime.strptime("2020-09-21", "%Y-%m-%d")

        stock = DailySummary.objects.get_stock_for_date(date, product=None)
        for l in stock.iterator():
            if l.product == self.product:
                self.assertEqual(l.stockEnd, 45)

    def test_receive_5(self):
        """
            Precondition: Execute 1 2 3
            Do: Receive production A4 80 GSM on 2oth September with rimps per carton 5, carton received:1, bonus units:0
            Validate:  In stock A4 80 GSM will be 65 on 21st Septermber.
        """

        Receive.objects.create(product=self.product, price=self.price, date="2020-09-21", unitPerPackage=5,
                               receivedPackage=5, unit=25)

        Receive.objects.create(product=self.product, price=self.price, date="2020-09-14", unitPerPackage=5,
                               receivedPackage=2, unit=10)

        Receive.objects.create(product=self.product, price=self.price, date="2020-09-20", unitPerPackage=5,
                               receivedPackage=5, unit=25)

        Receive.objects.create(product=self.product, price=self.price, date="2020-09-20", unitPerPackage=5,
                               receivedPackage=1, unit=5)
        date = datetime.strptime("2020-09-21", "%Y-%m-%d")

        stock = DailySummary.objects.get_stock_for_date(date, product=None)
        for l in stock.iterator():
            if l.product == self.product:
                self.assertEqual(l.stockEnd, 65)


    def test_receive_6(self):
        """
             Do: Receive a product A4 80 GSM with Rims per carton: 5, Cartons received: 5, Bonus Units: 5, Date: 21st September, 2020.
            Validate: In stock A4 80 GSM will be 25, in daily summary for 21st September Stock end will be 30.
        """

        Receive.objects.create(product=self.product, price=self.price, date="2020-09-21", unitPerPackage=5,
                               receivedPackage=5, unit=25, bonusUnits=5)
        date = datetime.strptime("2020-09-21", "%Y-%m-%d")

        stock = DailySummary.objects.get_stock_for_date(date, product=None)
        for l in stock.iterator():
            if l.product == self.product:
                self.assertEqual(l.stockEnd, 30)

    def test_receive_7(self):
        """
            Precondition: Execute 6
            Do: Receive a product A4 80 GSM on 14th Semptember 2020, with rimps per carton: 5, carton received: 2, bonus units: 10.
            Validate: In stock A4 80 GSM will be 50 on 21st September.
        """

        Receive.objects.create(product=self.product, price=self.price, date="2020-09-21", unitPerPackage=5,
                               receivedPackage=5, unit=25, bonusUnits=5)

        Receive.objects.create(product=self.product, price=self.price, date="2020-09-15", unitPerPackage=5,
                               receivedPackage=2, unit=10, bonusUnits=10)

        date = datetime.strptime("2020-09-21", "%Y-%m-%d")

        stock = DailySummary.objects.get_stock_for_date(date, product=None)
        for l in stock.iterator():
            if l.product == self.product:
                self.assertEqual(l.stockEnd, 50)

    def test_receive_8(self):
        """
            Precondition: Execute 6, 7
            Do: Update receive product for A4 80 GSM on 14th september 2020, set bonus unit: 5
            Validate: In stock A4 80 GSM will be 45 on 21st September
        """

        Receive.objects.create(product=self.product, price=self.price, date="2020-09-21", unitPerPackage=5,
                               receivedPackage=5, unit=25, bonusUnits=5)

        rcv = Receive.objects.create(product=self.product, price=self.price, date="2020-09-15", unitPerPackage=5,
                               receivedPackage=2, unit=10, bonusUnits=10)

        rcv.bonusUnits = 5
        rcv.save()

        date = datetime.strptime("2020-09-21", "%Y-%m-%d")

        stock = DailySummary.objects.get_stock_for_date(date, product=None)
        for l in stock.iterator():
            if l.product == self.product:
                self.assertEqual(l.stockEnd, 45)

    def test_receive_9(self):
        """
            Precondition: Execute 6, 7
            Do: Update receive product for A4 80 GSM on 14th september 2020, set bonus unit: 15
            Validate: In stock A4 80 GSM will be 55 on 21st September
        """

        Receive.objects.create(product=self.product, price=self.price, date="2020-09-21", unitPerPackage=5,
                               receivedPackage=5, unit=25, bonusUnits=5)

        rcv = Receive.objects.create(product=self.product, price=self.price, date="2020-09-15", unitPerPackage=5,
                               receivedPackage=2, unit=10, bonusUnits=10)

        rcv.bonusUnits = 15
        rcv.save()

        date = datetime.strptime("2020-09-21", "%Y-%m-%d")

        stock = DailySummary.objects.get_stock_for_date(date, product=None)
        for l in stock.iterator():
            if l.product == self.product:
                self.assertEqual(l.stockEnd, 55)

    def test_receive_10(self):
        """
            Precondtion: Execute 6, 7
            Do: Receive product A4 80 GSM on 17th september 2020, with unitPerPackage:5, receivedPackage:3, bonusUnits: 10
            Validate:  In stock A4 80 GSM will be 75 on 21st September
        :return:
        """

        Receive.objects.create(product=self.product, price=self.price, date="2020-09-21", unitPerPackage=5,
                               receivedPackage=5, unit=25, bonusUnits=5)

        Receive.objects.create(product=self.product, price=self.price, date="2020-09-15", unitPerPackage=5,
                               receivedPackage=2, unit=10, bonusUnits=10)

        Receive.objects.create(product=self.product, price=self.price, date="2020-09-17", unitPerPackage=5,
                               receivedPackage=3, unit=15, bonusUnits=10)

        date = datetime.strptime("2020-09-21", "%Y-%m-%d")

        stock = DailySummary.objects.get_stock_for_date(date, product=None)
        for l in stock.iterator():
            if l.product == self.product:
                self.assertEqual(l.stockEnd, 75)













