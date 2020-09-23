from catalogue.models import Product, Price
from operation.models import Receive, DailySummary, Issue


def run():
    product = Product.objects.get(id=3)
    price = Price.objects.get(id=1)

    DailySummary.objects.all().delete()
    Receive.objects.all().delete()
    Issue.objects.all().delete()

    Receive.objects.create(product=product, price=price, date="2020-09-21", unitPerPackage=5,
                           receivedPackage=2, unit=10, bonusUnits=5)
    Receive.objects.create(product=product, price=price, date="2020-09-15", unitPerPackage=5,
                           receivedPackage=2, unit=10, bonusUnits=5)
    Receive.objects.create(product=product, price=price, date="2020-09-10", unitPerPackage=5,
                           receivedPackage=2, unit=10, bonusUnits=5)

    iss = Issue.objects.create(product=product, price=price, date="2020-09-17", unit=10)







