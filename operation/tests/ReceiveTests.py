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








