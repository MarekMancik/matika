from django.shortcuts import render
from mathapp.math_models import MathCase

# Create your views here.

def generate_math_examples(request):
    if request == "POST":
        addition_example = MathCase.addition(numeric_range_low=0, numeric_range_high=20)

        # place for mathematic examples
        math_examples = {"Příklad": addition_example, }

    return render(request, "math_examples.html", math_examples)

