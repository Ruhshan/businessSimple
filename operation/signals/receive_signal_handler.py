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

    update_stock_for_product_after_date(instance.product, instance.unit, instance.date)


def insert_top(instance):
    obj, created = summary_get_or_create(instance.product, instance.date)
    if created:
        obj.stockStart = 0
        obj.stockEnd = instance.unit
        obj.totalReceived = instance.unit
        obj.save()
    else:
        obj.stockEnd = obj.stockEnd + instance.unit
        obj.totalReceived = obj.totalReceived + instance.unit
        obj.save()


def insert_within(instance):
    last_summary = get_last_summary(instance)
    obj, created = summary_get_or_create(instance.product, instance.date)
    if created:
        obj.stockStart = last_summary.stockEnd
        obj.stockEnd = last_summary.stockEnd + instance.unit
        obj.totalReceived = instance.unit
        obj.save()
    else:
        obj.stockEnd = obj.stockEnd + instance.unit
        obj.totalReceived = obj.totalReceived + instance.unit
        obj.save()


def summary_get_or_create(product, date):
    return DailySummary.objects.get_or_create(product=product, date=date)


def update_stock_for_product_after_date(product, unit, date):
    updatables = DailySummary.objects.filter(product=product, date__gt=date)

    if updatables.exists():
        updatables.update(stockStart = F('stockStart')+unit, stockEnd = F('stockEnd')+unit)


def get_last_summary(instance):
    return DailySummary.objects.filter(product=instance.product, date__lt=instance.date).order_by('date').last()


def handle_instance_update(instance):
    old_instance = Receive.objects.get(id = instance.id)
    if old_instance.date != instance.date and old_instance.unit == instance.unit:
        handle_date_update(old_instance, instance)
    elif old_instance.date == instance.date and old_instance.unit != instance.unit:
        handle_unit_change(old_instance, instance)
    elif old_instance.date != instance.date and old_instance.unit != instance.unit:
        handle_date_unit_update(old_instance, instance)
    else:
        pass


def handle_date_update(old_instance, new_instance):
    pass


def handle_unit_change(old_instance, new_instance):
    difference = new_instance.unit - old_instance.unit
    daily_summary = DailySummary.objects.get(date=new_instance.date, product=old_instance.product)

    daily_summary.stockEnd += difference
    daily_summary.totalReceived += difference

    daily_summary.save()

    update_stock_for_product_after_date(new_instance.product, difference, new_instance.date)



def handle_date_unit_update(old_instance, new_instance):
    pass

