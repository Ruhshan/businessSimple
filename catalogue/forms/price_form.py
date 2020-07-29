from django.forms import ModelForm
from catalogue.models import Price
from report.widgets import BootstrapDateTimePickerInput


class PriceForm(ModelForm):
    class Meta:
        model = Price
        fields = ['product', 'validFrom', 'validThrough', 'buying', 'selling', 'isActive']
        widgets = {
            'validFrom': BootstrapDateTimePickerInput(),
            'validThrough': BootstrapDateTimePickerInput()
        }