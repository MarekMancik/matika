from django.shortcuts import render, HttpResponse
from mathapp.math_models import MathCase
from sympy import sympify

# Create your views here.

def generate_math_examples(request):
    # receive a requirement regarding generatin of math examples - typ, range, count
    if request.method == "POST":
        addition_example = MathCase.addition(count=5, numeric_range_low=0, numeric_range_high=20)
        print(f"Obsah listu na začátku:{addition_example}")

        # place for mathematic examples
        math_examples = {"examples": addition_example}
        # print(math_examples)

        return render(request, "math_examples.html", context=math_examples)



def validation_math_examples(request):
    # receive complete generate examples plus results from user. The result are validate
    if request.method == "POST":
        examples = request.POST.getlist('example')
        results = request.POST.getlist('result')
        print(f"Přijaté výsledky: {examples}{results},")

        # the union of two list
        # for exampl, result in zip(examples, results):
        #     print(exampl, result)
        # validation of examples:
        for exampl, result in zip(examples, results):

            if eval(exampl) == int(result):
                print(exampl, result, "OK")
            else:
                print(exampl, result, "NOK")

        return render(request, 'validation_math_examples.html')