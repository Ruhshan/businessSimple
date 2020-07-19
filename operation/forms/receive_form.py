from django.forms import ModelForm, ValidationError
from operation.models import Receive
import datetime


class ReceiveForm(ModelForm):
    def clean_date(self):
        today = datetime.datetime.today().date()
        form_date = self.cleaned_data['date']
        if today < form_date:
            raise ValidationError("Future date is not allowed")
        return form_date

    class Meta:
        model = Receive
        fields = ['product', 'unit', 'date', 'receipt_no']