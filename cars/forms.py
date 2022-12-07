from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cars, ApplicationUser
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
                  'previous_owners', 'image',)


class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input-text with-border', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input-text with-border', 'placeholder': 'Repeat Password'}))

    class Meta:
        model = User
        fields = 'username', 'email'


COUNTRY_CHOICES = (
    ("FR", "France"),
    ("DE", "Germany"),
    ("AL", "Albania"),
    ("BE", "Belgium"),
    ("NL", "Nederland"),
    ("IT", "Italy"),
)


class RegUsers(forms.ModelForm):
    phone = forms.IntegerField()
    address = forms.CharField()
    city = forms.CharField()
    zip_code = forms.CharField()
    country = forms.ChoiceField(choices=COUNTRY_CHOICES)

    class Meta:
        model = ApplicationUser
        fields = ('phone', 'address', 'city', 'zip_code', 'country')
