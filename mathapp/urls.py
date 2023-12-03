from django.urls import path
from .views import buttons_response, validation_math_examples

urlpatterns = [
    path('generate_math_examples/', buttons_response, name='buttons_response'),
    path('validation_math_examples/', validation_math_examples, name='validation_math_examples')
]