from cars.forms import CreateUserForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render


def LoginClient(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cars')

    return render(request, 'loginclient.html')


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
    return render(request, 'register.html', context)
