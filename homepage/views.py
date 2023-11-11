import json
from django.http import HttpResponse
from django.shortcuts import render

from todos.forms import RegistrationForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, template_name='index.html')


def test_form(request):
    button_response = request.POST.dict()
    print(f"Byla aktivována tato tlačítka: {button_response}")
    return HttpResponse("Data byla přijata!")


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            gender = form.cleaned_data['gender']
            password = form.cleaned_data['password']

            # created a new user
            user = User.objects.create_user(
                username=email,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
                gender=gender
            )

            return render(request, 'success_registration.html', {'user': user})
    else:
        # create new registration form
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})