from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

from .models import Car, Driver


class LicenseForm(forms.Form):
    def clean_license_number(self):
        license_number = self.cleaned_data.get("license_number")
        if len(license_number) != 8:
            raise ValidationError(
                "License number should consist of 8 characters"
            )
        if not license_number[:3].isupper():
            raise ValidationError(
                "First 3 characters should be uppercase letters"
            )
        if not license_number[3:].isdigit():
            raise ValidationError("Last 5 characters should be digits")
        return license_number


class DriverCreationForm(LicenseForm, UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields + ("license_number",)


class DriverLicenseUpdateForm(LicenseForm, forms.ModelForm):

    class Meta:
        model = Driver
        fields = ("license_number",)


class CarCreateForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Car
        fields = "__all__"
