from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cars, Messages
from django.contrib.auth.models import User


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


class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ('text', 'recipient')

    # widgets = {
    #     'recipient': forms.HiddenInput({'recipient': 'username.'}), }
