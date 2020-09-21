from django.test import TestCase

from catalogue.models import Product, Price
from operation.models import Receive, DailySummary
from datetime import datetime

class ReceiveTests(TestCase):
    def setUp(self) -> None:
        self.product = Product.objects.create(name="A4 80 GSM")
        self.price = Price.objects.create(product=self.product, buying=5, selling=5, validFrom="2020-08-21", validThrough="2020-12-21")

    def test_receive(self):
        receive = Receive.objects.create(product=self.product, price=self.price, date="2020-09-21", unitPerPackage=5,
                                         receivedPackage=5, unit=25)
        date = datetime.strptime("2020-09-21", "%Y-%m-%d")

        stock = DailySummary.objects.get_stock_for_date(date, product=None)
        for l in stock.iterator():
            if l.product == self.product:
                self.assertEqual(l.stockEnd, receive.unit)

        ds = DailySummary.objects.filter(product=self.product, date=date).first()
        self.assertEqual(ds.stockEnd, receive.unit)



