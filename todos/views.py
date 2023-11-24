from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, redirect

from todos.forms import RegistrationForm
from todos.models import User
from django.contrib.auth import authenticate, login


# Create your views here.
def index(request):
    return render(request, template_name='buttons_page.html')


def test_form(request):
    button_response = request.POST.getlist('button')
    range_values = request.POST.getlist('range')
    print(f"Byla aktivována tato tlačítka: {button_response}")
    print(f"Hodnoty range tlačítek jsou: {range_values}")
    return HttpResponse(f"Data byla přijata! {button_response}, {range_values}")


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            # gender = form.cleaned_data['gender']
            password = form.cleaned_data['password']

            # created a new user
            user = User.objects.create_user(
                username=email,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
                # gender=gender
            )
            # user.save() # dont use, because create_user save the data automatic

            return render(request, 'success_registration.html', {'user': user})
    else:
        # create new registration form
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        user_email = request.POST.get('login_email')
        user_password = request.POST.get('login_password')

        print(f"email uživatele je: {user_email} a jeho heslo je {user_password}")
        user = authenticate(request, username=user_email, password=user_password)

        print(user)

        if user is not None:
            login(request, user)
            print('úspěšné přihlášení')
            return redirect('base')

        else:
            print("špatný email, nebo heslo, zkuste to prosím znovu")
            return redirect('base')

    return render(request, 'base')