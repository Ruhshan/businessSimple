from operation.models import Return, DailySummary
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db.models import F


@receiver(pre_save, sender=Return)
def return_save_handler(sender, instance, **kwargs):
    if instance.id:
        handle_instance_update(instance)
    else:
        handle_instance_creation(instance)


def handle_instance_creation(instance):
    obj, created = summary_get_or_create(instance.product, instance.date)
    if created:
        last_summary = get_last_summary(instance)
        obj.stockStart = last_summary.stockEnd
        obj.stockEnd = last_summary.stockEnd + instance.unit
        obj.totalIssued = instance.unit
        obj.save()
    else:
        obj.stockEnd += instance.unit
        obj.totalReturned += instance.unit
        obj.save()

    update_stock_for_product_after_date(instance.product, instance.unit, instance.date)


def get_last_summary(instance):
    return DailySummary.objects.filter(product=instance.product, date__lt=instance.date).order_by('date').last()


def update_stock_for_product_after_date(product, unit, date):
    updatables = DailySummary.objects.filter(product=product, date__gt=date)

    if updatables.exists():
        updatables.update(stockStart=F('stockStart') + unit, stockEnd=F('stockEnd') + unit)


def summary_get_or_create(product, date):
    return DailySummary.objects.get_or_create(product=product, date=date)


def handle_instance_update(new_instance):
    old_instance = Return.objects.get(id=new_instance.id)
    daily_summary_old = DailySummary.objects.get(product=old_instance.product, date=old_instance.date)
    daily_summary_old.stockEnd -= old_instance.unit
    daily_summary_old.totalReturned -= old_instance.unit
    daily_summary_old.save()

    update_stock_for_product_after_date(old_instance.product, 1 * old_instance.unit, old_instance.date)

    handle_instance_creation(new_instance)
