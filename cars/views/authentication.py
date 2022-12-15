from cars.forms import CreateUserForm
from cars.models import Cars
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def LoginClient(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cars')

    return render(request, 'user/loginclient.html')


def LogoutClient(request):
    logout(request)
    return redirect('cars')


# todo: Rinderto duke perdorur django forms.
def RegClients(request):
    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    else:
        user_form = CreateUserForm()
    context = {'user_form': user_form}
    return render(request, 'user/register.html', context)


def Profile(request, pk):
    user_profile = User.objects.get(id=pk)
    cars = Cars.objects.filter(owner=user_profile)

    return render(request, 'user/profile.html', {'user_profile': user_profile, 'cars': cars})
