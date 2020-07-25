from django import forms
from catalogue.models.product_model import Product

from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap
from crispy_forms.bootstrap import InlineField, FormActions, StrictButton, Div
from crispy_forms.layout import Layout
from crispy_forms import bootstrap, layout
from crispy_forms.layout import Layout, Submit, Row, Column
from report.widgets import BootstrapDateTimePickerInput



class StockReportForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), required=False)
    date = forms.DateTimeField(
        widget=BootstrapDateTimePickerInput(),
        required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()


        self.helper.layout = Layout(
            Row(
                Column('product', css_class='form-group col-md-4 mb-0'),
                Column('date', css_class='form-group col-md-4 mb-0'),
                Column(
                    bootstrap.FormActions(
                        layout.Submit('submit', 'Search', css_class='btn btn-primary')),
                    css_class='search-button'
                ),
                css_class='form-row',

            )
        )