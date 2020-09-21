from operation.models import Receive, DailySummary
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db.models import F


@receiver(pre_save, sender = Receive)
def receive_save_handler(sender, instance, **kwargs):
    if instance.id:
        handle_instance_update(instance)
    else:
        handle_instance_creation(instance)


def handle_instance_creation(instance):
    if DailySummary.objects.filter(product=instance.product, date__lt=instance.date).exists():
        insert_within(instance)
    else:
        insert_top(instance)

    update_stock_for_product_after_date(instance.product, instance.unit + instance.bonusUnits, instance.date)


def insert_top(instance):
    obj, created = summary_get_or_create(instance.product, instance.date)
    if created:
        obj.stockStart = 0
        obj.stockEnd = instance.unit + instance.bonusUnits
        obj.totalReceived = instance.unit
        obj.bonusReceived = instance.bonusUnits
        obj.save()
    else:
        obj.stockEnd = obj.stockEnd + instance.unit + instance.bonusUnits
        obj.totalReceived = obj.totalReceived + instance.unit
        obj.bonusReceived = obj.bonusReceived + instance.bonusUnits
        obj.save()


def insert_within(instance):
    last_summary = get_last_summary(instance)
    obj, created = summary_get_or_create(instance.product, instance.date)
    if created:
        obj.stockStart = last_summary.stockEnd
        obj.stockEnd = last_summary.stockEnd + instance.unit + instance.bonusUnits
        obj.totalReceived = instance.unit
        obj.bonusReceived = instance.bonusUnits
        obj.save()
    else:
        obj.stockEnd = obj.stockEnd + instance.unit + instance.bonusUnits
        obj.totalReceived = obj.totalReceived + instance.unit
        obj.bonusReceived = obj.bonusReceived + instance.bonusUnits
        obj.save()


def summary_get_or_create(product, date):
    return DailySummary.objects.get_or_create(product=product, date=date)


def update_stock_for_product_after_date(product, unit, date):
    updatables = DailySummary.objects.filter(product=product, date__gt=date)

    if updatables.exists():
        updatables.update(stockStart = F('stockStart')+unit, stockEnd = F('stockEnd')+unit)


def get_last_summary(instance):
    return DailySummary.objects.filter(product=instance.product, date__lt=instance.date).order_by('date').last()


def handle_instance_update(new_instance):
    old_instance = Receive.objects.get(id = new_instance.id)
    daily_summary_old = DailySummary.objects.get(product=old_instance.product, date=old_instance.date)
    daily_summary_old.stockEnd -= old_instance.unit
    daily_summary_old.totalReceived -= old_instance.unit
    daily_summary_old.bonusReceived -= old_instance.bonusUnits
    daily_summary_old.save()

    update_stock_for_product_after_date(old_instance.product, old_instance.unit+old_instance.bonusUnits, old_instance.date)

    handle_instance_creation(new_instance)


