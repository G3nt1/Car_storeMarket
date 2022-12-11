from cars.forms import CreateUserForm, RegUsers
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
        profile_form = RegUsers(request.POST)
        if profile_form.is_valid() and user_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.username = user
            profile.email = user.email
            profile.phone = request.POST['phone']
            profile.address = request.POST['address']
            profile.city = request.POST['city']
            profile.zip_code = request.POST['zip_code']
            profile.country = request.POST['country']
            profile.save()
            return redirect('login')
    else:
        user_form = CreateUserForm()
        profile_form = RegUsers()
    context = {'user_form': user_form, 'form': profile_form}
    return render(request, 'register.html', context)
