from django.urls import path
from .views import generate_math_examples, validation_math_examples

urlpatterns = [
    path('generate_math_examples/', generate_math_examples, name='generate_math_examples'),
    path('validation_math_examples/', validation_math_examples, name='validation_math_examples')
]