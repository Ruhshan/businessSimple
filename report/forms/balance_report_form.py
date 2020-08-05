from django import forms
from catalogue.models.product_model import Product

from crispy_forms.helper import FormHelper
from crispy_forms import bootstrap, layout
from crispy_forms.layout import Layout, Submit, Row, Column
from report.widgets import BootstrapDateTimePickerInput

class BalanceReportForm(forms.Form):
    startDate = forms.DateTimeField(widget=BootstrapDateTimePickerInput(), required=True)
    endDate = forms.DateTimeField(widget=BootstrapDateTimePickerInput(), required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Row(
                Column('startDate', css_class='form-group col-md-4 mb-0'),
                Column('endDate', css_class='form-group col-md-4 mb-0'),
                Column(
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Generate', css_class='btn btn-primary')),
                    css_class='search-button'
                ),
                css_class='form-row',

            )
        )