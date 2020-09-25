from django.forms import ModelForm, ValidationError, Select
from operation.models import Issue, DailySummary
import datetime
from django.utils.translation import ugettext_lazy as _

from operation.widgets import VueSelect


class IssueForm(ModelForm):
    def clean_date(self):
        today = datetime.datetime.today().date()
        form_date = self.cleaned_data['date']
        form_product = self.cleaned_data['product']

        if today < form_date:
            raise ValidationError("Future date is not allowed")

        has_previous_summary = DailySummary.objects.has_previous_summary(form_product, form_date)

        if not has_previous_summary:
            raise ValidationError("No product in stock for this date")

        return form_date

    def clean_unit(self):
        if len(self.errors.keys()) == 0:
            form_date = self.cleaned_data['date']
            form_product = self.cleaned_data['product']
            summary_for_date = DailySummary.objects.get_summary_for_date(form_product, form_date)
            form_unit = self.cleaned_data['unit']
            if summary_for_date.stockEnd < form_unit:
                raise ValidationError(
                    _('Issuing more than %(value)s units is not possible for date %(date)s'),
                    params={'value': summary_for_date.stockEnd, 'date': form_date},
                )
            summaries_after_date = DailySummary.objects.get_summary_after_date(form_product, form_date)
            for obj in summaries_after_date:
                if obj.stockEnd < form_unit:
                    raise ValidationError(_('Issuing %(unit)s will make stocks negative on %(date)s'),
                                          params={'unit':form_unit,'date':form_date})

        return self.cleaned_data['unit']

    class Meta:
        model = Issue
        fields = ['product', 'price', 'date', 'unit', 'bonusUnits', 'receipt_no', 'customer','remarks']
        widgets = {
            'product': Select(attrs={'v-model': 'product'}),
            'price': VueSelect()
        }
