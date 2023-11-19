from django.shortcuts import render
from mathapp.math_models import MathCase
from time import time

# Create your views here.

def generate_math_examples(request):
    if request.method == "POST":
        addition_example = MathCase.addition(count=10, numeric_range_low=0, numeric_range_high=20)
        print(f"Obsah listu na začátku:{addition_example}")

    #     # place for mathematic examples
        math_examples = {"examples": addition_example}
        print(math_examples)

        return render(request, "math_examples.html", context=math_examples)
    # return render(request, "math_examples.html")
