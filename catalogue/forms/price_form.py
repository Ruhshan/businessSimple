from django.forms import ModelForm
from catalogue.models import Price
from report.widgets import BootstrapDateTimePickerInput


class PriceForm(ModelForm):
    def clean_validThrough(self):
        data = self.cleaned_data['validThrough']
        return data

    class Meta:
        model = Price
        fields = ['product', 'validFrom', 'validThrough', 'buying', 'selling', 'isActive']
        widgets = {
            'validFrom': BootstrapDateTimePickerInput(),
            'validThrough': BootstrapDateTimePickerInput()
        }