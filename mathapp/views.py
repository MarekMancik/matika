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
    # výpočet plus.
    if button_plus == "plus":
        count_button_plus = int(count_button_plus)
        print(f"Počet příkladů plus: {count_button_plus}")
        examples_plus = MathCase.addition(count=count_button_plus, numeric_range_low=low, numeric_range_high=high)
        math_examples.update({"examples_plus": examples_plus})


    # výpočet pro mínus
    if button_minus == "minus":
        count_button_minus = int(count_button_minus)
        print(f"Počet příkladů mínus: {count_button_minus}")
        examples_minus = MathCase.substraction(count=count_button_minus, numeric_range_low=low, numeric_range_high=high)
        math_examples.update({"examples_minus": examples_minus})

    print(math_examples)

    return render(request, "math_examples.html", context=math_examples)

def generate_math_examples(request):
    pass


#     print(f"výpis buttons response {buttons_response(request)}")
#
#     # aktivace funkce buttons_response() s parametrem request, výsledkem je tuple všech aktivních tlačítek
#     response = buttons_response(request)
#
#     # počet příkladů pro jednotlivé mat. operace
#     resp = get_number_of_examples()
#     num_plus, num_minus, num_krat, num_deleno = resp[1], resp[2], resp[3], resp[4]
#
#     # spuštění funkce pro určení číselného oboru get_numeric_range()
#
#     response = buttons_response(request)
#
#     count_plus = response[1][0]
#     print(f"[1] prvek response: {count_plus}")
#
#     addition_example = [10, 15, 7, 8, 9, 12, 113]
#     math_examples = {"examples": addition_example}
#
#     return render(request, "math_examples.html", context=math_examples)


# def generate_math_examples(request):
#     # receive a requirement regarding generating of math examples - typ, range, count
#     if request.method == "POST":
#         addition_example = MathCase.addition(count=5, numeric_range_low=0, numeric_range_high=20)
#         print(f"Obsah listu na začátku:{addition_example}")
#
#         # place for mathematic examples
#         math_examples = {"examples": addition_example}
#         # print(math_examples)
#
#         return render(request, "math_examples.html", context=math_examples)


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
