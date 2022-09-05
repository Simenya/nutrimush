from django import forms
from django.forms import ModelForm
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Column, Row


class CustomerForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Customer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(
            Submit('submit', 'submit', css_class="btn btn-sm btn-danger w-25 offset-5"))

        self.helper.layout = Layout(
            Row(
                Column('name'),
                Column('phone'),
            ),
            Row(
                Column('address'),
                Column('email'),
            ),
        )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        phone = cleaned_data.get("phone")
        address = cleaned_data.get("address")
        email_address = cleaned_data.get("email_address")
        if not (phone or email_address):
            raise forms.ValidationError(
                "You must enter either a phone number or an email, or both."
            )


class OrderForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(
            Submit('submit', 'submit', css_class="btn btn-sm btn-danger w-25 offset-5"))

        self.helper.layout = Layout( 
            Row(
                Column('customers'),
                Column('products'),
            ),
            'status'
        )

    def clean(self):
        cleaned_data = super().clean()
        customers = cleaned_data.get("customers")
        products = cleaned_data.get("products")
        if not (customers or products):
            raise forms.ValidationError(
                "Some fields are missing."
            )
