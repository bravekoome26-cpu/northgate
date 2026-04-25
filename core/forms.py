from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Booking, FoodItem, Order, TableReservation


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")
    first_name = forms.CharField(required=False, label="First name")
    last_name = forms.CharField(required=False, label="Last name")

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")


class BookingForm(forms.ModelForm):
    check_in = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    check_out = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))

    class Meta:
        model = Booking
        fields = ("check_in", "check_out")

    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')
        if check_in and check_out and check_out <= check_in:
            raise forms.ValidationError('Check-out date must be after the check-in date.')
        return cleaned_data


class OrderForm(forms.ModelForm):
    items = forms.ModelMultipleChoiceField(
        queryset=FoodItem.objects.filter(available=True),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Order
        fields = ("items",)


class TableReservationForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={"type": "time"}))

    class Meta:
        model = TableReservation
        fields = ("guests", "date", "time")
