from django.shortcuts import render, HttpResponse
from mathapp.math_models import MathCase


# Create your views here.

def buttons_response(request):
    # request from buttons

    button_plus = request.POST.get("button_plus")
    button_minus = request.POST.get("button_minus")
    button_krat = request.POST.get("button_krat")
    button_deleno = request.POST.get("button_deleno")

    count_button_plus = request.POST.get("select_button_plus")
    count_button_minus = request.POST.get("select_button_minus")
    count_button_krat = request.POST.get("select_button_krat")
    count_button_deleno = request.POST.get("select_button_deleno")

    button_range = request.POST.get("button_range")

    button_over_10 = request.POST.get("button_over_10")

    # vyřeším button_range:přečíst a rozdělit na 0 a 10,
    low, high = 0, 0
    if button_range:
        if button_range == "range_0-10":
            low, high = 0, 10
        elif button_range == "range_0-20":
            low, high = 0, 20
        elif button_range == "range_0-100":
            low, high = 0, 100

    print(f"Kontrolní výpis, hodnota rozsahu: {low} a {high}")

    math_examples = {}
    examples = []
    # výpočet plus.
    if button_plus == "plus":
        count_button_plus = int(count_button_plus)
        print(f"Počet příkladů plus: {count_button_plus}")
        examples_plus = MathCase.addition(count=count_button_plus, numeric_range_low=low, numeric_range_high=high)
        # math_examples.update({"examples_plus": examples_plus})


    # výpočet pro mínus
    if button_minus == "minus":
        count_button_minus = int(count_button_minus)
        print(f"Počet příkladů mínus: {count_button_minus}")
        examples_minus = MathCase.substraction(count=count_button_minus, numeric_range_low=low, numeric_range_high=high)
        # math_examples.update({"examples_minus": examples_minus})

    if button_krat == "krat":
        count_button_krat = int(count_button_krat)
        print(f"Počet příkladů krat: {count_button_krat}")
        examples_krat = MathCase.multiplication(count=count_button_krat, numeric_range_low=low, numeric_range_high=high)

    print(math_examples)

    if 'examples_plus' in locals() and examples_plus is not None:
        examples.extend(examples_plus)

    if 'examples_minus' in locals() and examples_minus is not None:
        examples.extend(examples_minus)

    if 'examples_krat' in locals() and examples_krat is not None:
        examples.extend(examples_krat)

    print(f"list příkladů: {examples}")
    math_examples.update({"examples": examples})
    print(f"Dictionary příkazů: {math_examples}")
    # complete examples send to math_examples.html
    return render(request, "math_examples.html", context=math_examples)





def validation_math_examples(request):
    # receive complete generate examples plus results from user. The result are validate
    if request.method == "POST":
        examples = request.POST.getlist('example')
        results = request.POST.getlist('result')
        print(f"Přijaté výsledky: {examples}{results},")

        # the union of two list
        val_examples = []
        for exampl, result in zip(examples, results):
            if eval(exampl) == int(result):
                val_examples.append(f"{exampl} = {result} OK")
            else:
                val_examples.append(f"{exampl} = {result} NOK")
        validation_examples = {"validation_math_examples": val_examples}
        print(val_examples)
        print(validation_examples)
        return render(request, 'validation_math_examples.html', context=validation_examples)
        # return render(request, 'math_examples.html', context=validation_examples)


def generate_math_examples(request):
    pass



