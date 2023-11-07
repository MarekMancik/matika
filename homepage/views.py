import json
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, template_name='index.html')


def test_form(request):
    button_response = request.POST.dict()
    print(f"Byla aktivována tato tlačítka: {button_response}")
    return HttpResponse("Data byla přijata!")
