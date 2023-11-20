from django.shortcuts import render, HttpResponse
from mathapp.math_models import MathCase


# Create your views here.

def generate_math_examples(request):
    # receive a requirement regarding generatin of math examples - typ, range, count
    if request.method == "POST":
        addition_example = MathCase.addition(count=5, numeric_range_low=0, numeric_range_high=20)
        # print(f"Obsah listu na začátku:{addition_example}")

        # place for mathematic examples
        math_examples = {"examples": addition_example}
        # print(math_examples)

        return render(request, "math_examples.html", context=math_examples)



def validation_math_examples(request):
    # receive complete generate examples plus results from user. The result are validate
    if request.method == "POST":
        results = request.POST.getlist('result')
        print(f"Přijaté výsledky: {results}")
        return render(request, 'validation_math_examples.html')
