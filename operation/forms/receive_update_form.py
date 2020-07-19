from django.forms import ModelForm, ValidationError
from operation.models import Receive
import datetime

class ReceiveUpdateForm(ModelForm):
    def clean_date(self):
        today = datetime.datetime.today().date()
        form_date = self.cleaned_data['date']
        if today < form_date:
            raise ValidationError("Future date is not allowed")
        return form_date

    def clean_unit(self):
        form_unit = self.cleaned_data['unit']
        if form_unit<0:
            raise ValidationError("Unit cannot be negative")
        return form_unit

    class Meta:
        model = Receive
        fields = ['product', 'unit', 'date', 'receipt_no']