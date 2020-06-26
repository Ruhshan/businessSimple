from catalogue.models import Vendor
import random
import string

def run():
    for i in range(10):
        name=randomString(5)
        phone = randomString(10)
        Vendor.objects.create(name=name,phone=phone,email=name+"@mail.com")

def randomString(stringLength=5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
