from django.forms import ModelForm, ValidationError, Select
from operation.models import Return
import datetime

from operation.widgets import VueSelect


class ReturnForm(ModelForm):
    def clean_date(self):
        today = datetime.datetime.today().date()
        form_date = self.cleaned_data['date']
        if today < form_date:
            raise ValidationError("Future date is not allowed")
        return form_date

    class Meta:
        model = Return
        fields = ['product', 'unit', 'price','date', 'receipt_no', 'customer', 'remarks']
        widgets = {
            'product': Select(attrs={'v-model': 'product'}),
            'price': VueSelect()
        }