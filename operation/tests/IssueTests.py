from django.test import TestCase
from catalogue.models import Product, Price
from operation.models import Receive, DailySummary, Issue
from datetime import datetime


class IssueTests(TestCase):
    def setUp(self) -> None:
        self.product = Product.objects.create(name="A4 80 GSM")
        self.price = Price.objects.create(product=self.product, buying=5, selling=5, validFrom="2020-08-21",
                                          validThrough="2020-12-21")

    def test_01(self):
        """
        Do: Receive a product A4 80 GSM with Rims per carton: 5, Cartons received: 5, Bonus Units: 10, Date: 21st September, 2020.
            Issue a product A4 80 GSM with units 10 and date 22nd September, 2020
        Validate: In Stock A4 80 GSM will be 25 on 22nd September 2020.
        """
        Receive.objects.create(product=self.product, price=self.price, date="2020-09-21", unitPerPackage=5,
                               receivedPackage=5, unit=25, bonusUnits=10)
        Issue.objects.create(product=self.product, price=self.price, date="2020-09-22",unit=10)

        date = datetime.strptime("2020-09-22", "%Y-%m-%d")

        stock = DailySummary.objects.get_stock_for_date(date, product=None)
        for l in stock.iterator():
            if l.product == self.product:
                self.assertEqual(l.stockEnd, 25)

    def test_02(self):
        """
        Do: Receive A4 80 GSM on 21st Semptember, 2020, 15th September 2020, and 10th Septermber 2020 with 10 in units and 5 in bonus.
            Issue A4 80 GSM with 10 unit on 17th September, 2020.
        Validate: In stock A4 80 GSM will be 35 on 22nd September 2020
        """
        Receive.objects.create(product=self.product, price=self.price, date="2020-09-21", unitPerPackage=5,
                               receivedPackage=2, unit=10, bonusUnits=5)
        Receive.objects.create(product=self.product, price=self.price, date="2020-09-15", unitPerPackage=5,
                               receivedPackage=2, unit=10, bonusUnits=5)
        Receive.objects.create(product=self.product, price=self.price, date="2020-09-10", unitPerPackage=5,
                               receivedPackage=2, unit=10, bonusUnits=5)

        Issue.objects.create(product=self.product, price=self.price, date="2020-09-17", unit=10)

        date = datetime.strptime("2020-09-22", "%Y-%m-%d")

        stock = DailySummary.objects.get_stock_for_date(date, product=None)
        for l in stock.iterator():
            if l.product == self.product:
                self.assertEqual(l.stockEnd, 35)

    def test_03(self):
        """
        Do: Execute 1 and 2. Update Issue on 2020-09-17 , set unit to 15
        Validate: In stock A4 80 GSM will be 30 on 22nd September 2020
        """
        Receive.objects.create(product=self.product, price=self.price, date="2020-09-21", unitPerPackage=5,
                               receivedPackage=2, unit=10, bonusUnits=5)
        Receive.objects.create(product=self.product, price=self.price, date="2020-09-15", unitPerPackage=5,
                               receivedPackage=2, unit=10, bonusUnits=5)
        Receive.objects.create(product=self.product, price=self.price, date="2020-09-10", unitPerPackage=5,
                               receivedPackage=2, unit=10, bonusUnits=5)

        iss = Issue.objects.create(product=self.product, price=self.price, date="2020-09-17", unit=10)

        iss.unit = 15
        iss.save()

        date = datetime.strptime("2020-09-22", "%Y-%m-%d")

        stock = DailySummary.objects.get_stock_for_date(date, product=None)
        for l in stock.iterator():
            if l.product == self.product:
                self.assertEqual(l.stockEnd, 30)

    def test_04(self):
        """
        Do: Execute 1 and 2, Update Issue on 2020-09-17 , set unit to 5
        Validate: In stock A4 80 GSM will be 40 on 22nd September 2020
        """

        Receive.objects.create(product=self.product, price=self.price, date="2020-09-21", unitPerPackage=5,
                               receivedPackage=2, unit=10, bonusUnits=5)
        Receive.objects.create(product=self.product, price=self.price, date="2020-09-15", unitPerPackage=5,
                               receivedPackage=2, unit=10, bonusUnits=5)
        Receive.objects.create(product=self.product, price=self.price, date="2020-09-10", unitPerPackage=5,
                               receivedPackage=2, unit=10, bonusUnits=5)

        iss = Issue.objects.create(product=self.product, price=self.price, date="2020-09-17", unit=10)

        iss.unit = 5
        iss.save()

        date = datetime.strptime("2020-09-22", "%Y-%m-%d")

        stock = DailySummary.objects.get_stock_for_date(date, product=None)
        for l in stock.iterator():
            if l.product == self.product:
                self.assertEqual(l.stockEnd, 40)




