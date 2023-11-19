from django.urls import path
from .views import generate_math_examples

urlpatterns = [
    path('generate_math_examples/', generate_math_examples, name='generate_math_examples'),
]