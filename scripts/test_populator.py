
from catalogue.models import Product, Price
from operation.models import Receive, DailySummary
def run():
    a480gsm = Product.objects.get(id=3)
    a480gsm_price = Price.objects.get(id=1)

    DailySummary.objects.all().delete()
    Receive.objects.all().delete()

    Receive.objects.create(product=a480gsm, price=a480gsm_price, date="2020-09-21", unitPerPackage=5,
                           receivedPackage=5, unit=25)

    Receive.objects.create(product=a480gsm, price=a480gsm_price, date="2020-09-14", unitPerPackage=5,
                           receivedPackage=2, unit=10)

    Receive.objects.create(product=a480gsm, price=a480gsm_price, date="2020-09-20", unitPerPackage=5,
                           receivedPackage=5, unit=25)


