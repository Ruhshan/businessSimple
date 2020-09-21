from django.forms import ModelForm, ValidationError, Select, ChoiceField
from operation.models import Receive
import datetime
from operation.widgets import VueSelect


class ReceiveForm(ModelForm):

    def clean_date(self):
        today = datetime.datetime.today().date()
        form_date = self.cleaned_data['date']
        if today < form_date:
            raise ValidationError("Future date is not allowed")
        return form_date

    class Meta:
        model = Receive
        fields = ['product', 'price', 'unitPerPackage', 'receivedPackage', 'unit','bonusUnits', 'date', 'receipt_no']
        widgets = {
            'product': Select(attrs={'v-model':'product'}),
            'price':VueSelect()
        }