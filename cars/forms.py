from PIL.ImImagePlugin import number
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.http import request

from .models import Cars, Messages
from django.contrib.auth.models import User
from django.template.defaultfilters import format


class RegCar(forms.ModelForm):
    image = forms.ImageField(
        label="Image",
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
    )

    class Meta:
        model = Cars
        fields = ('brand', 'model', 'fuel_type', 'mileage',
                  'gearbox', 'year', 'motor', 'price', 'seller',
                  'doors', 'seats', 'color', 'features',
                  'previous_owners', 'address', 'city',
                  'zip_code', 'country', 'image')


class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input-text with-border', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input-text with-border', 'placeholder': 'Repeat Password'}))

    class Meta:
        model = User
        fields = 'username', 'email', 'first_name', 'last_name'


class MessageForm(forms.Form):
    recipient = received_messages__recipient = request.user()
    sender = sent_messages__sender = request.user()
    text = forms.CharField(max_length=500)

    class Meta:
        model = Messages
        fields = '__all__'
