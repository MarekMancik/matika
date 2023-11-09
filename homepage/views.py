import json
from django.http import HttpResponse
from django.shortcuts import render

from todos.forms import RegistrationForm


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
            # Create a new user
            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )
            # You can customize this part based on your needs
            return render(request, 'registration/success.html', {'user': user})
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})