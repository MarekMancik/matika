from django.shortcuts import render, HttpResponse
from mathapp.math_models import MathCase


# Create your views here.

def buttons_response(request):
    # request from buttons
    dict_buttons_response = request.POST.items()
    print(f"položka item() vypadá: {dict_buttons_response}")

    for key, value in dict_buttons_response:
        print(f"key:{key}, value:{value}")

    math_operation_buttons = request.POST.getlist('button')
    number_of_examples_plus = request.POST.getlist('select_button_plus')
    number_of_examples_minus = request.POST.getlist('select_button_minus')
    number_of_examples_krat = request.POST.getlist('select_button_krat')
    number_of_examples_deleno = request.POST.getlist('select_button_deleno')
    numeric_range = request.POST.getlist('button_2')

    # control print
    print(f"Byla aktivována tato tlačítka: {math_operation_buttons}")
    print(f"počet příkladů: {number_of_examples_plus}")
    print(f"další tlačítka:{numeric_range}")

    return math_operation_buttons, \
        number_of_examples_plus, \
        number_of_examples_minus, \
        number_of_examples_krat, \
        number_of_examples_deleno, \
        numeric_range

    # return HttpResponse(f"Data byla přijata! {math_operation_buttons}, {number_of_examples}, {numeric_range}")


def get_number_of_examples(tuple_of_plus, tuple_of_minus, tuple_of_krat, tuple_of_deleno):
    # reading select buttons for count of examples from tuple. Every tuple has only one value!!!
    # set number of examples translate from list to int
    num_examples_plus = int(tuple_of_plus[0])
    num_examples_minus = int(tuple_of_minus[0])
    num_examples_krat = int(tuple_of_krat[0])
    num_examples_deleno = int(tuple_of_deleno[0])

    return num_examples_plus, num_examples_minus, num_examples_krat, num_examples_deleno


def get_numeric_range(tuple_of_numeric_range):
    # reading buttons for numeric_range, tuple has always only one value!!!
    for every_range in tuple_of_numeric_range:
        if every_range == "range_0-10":
            return "0-10"
        elif every_range == "range_0-20":
            return "0-20"
        elif every_range == "range_0-100":
            return "0-100"


def get_math_examples(tuple_of_math_operations, result_of_get_numeric_range, result_of_get_number_of_examples):
    # math examples - count solve here

    # 1.get range of example
    num_range = result_of_get_numeric_range.split('-')  # num_range is List with two values
    num_low = int(num_range[0])
    num_high = int(num_range[1])

    # 2. get number of example for each math operation
    # Tuple is (plus, minus, krat, deleno)
    count_plus = result_of_get_number_of_examples[0]
    count_minus = result_of_get_number_of_examples[1]
    count_krat = result_of_get_number_of_examples[2]
    count_deleno = result_of_get_number_of_examples[3]

    # 3. look at the type of math operations
    for math_operation in tuple_of_math_operations:
        # musím se podívat do tuplu, které mat. funkce uživatel zvolil
        if math_operation == "plus":
            MathCase.addition(count=count_plus, numeric_range_low=num_low, numeric_range_high=num_high)
        elif math_operation == "minus":
            MathCase.substraction(count=count_minus, numeric_range_low=num_low, numeric_range_high=num_high)
        elif math_operation == "krat":
            MathCase.multiplication(count=count_krat, numeric_range_low=num_low, numeric_range_high=num_high)
        elif math_operation == "deleno":
            MathCase.division(count=count_deleno, numeric_range_low=num_low, numeric_range_high=num_high)


def generate_math_examples(request):
    print(f"výpis buttons response {buttons_response(request)}")

    # aktivace funkce buttons_response() s parametrem request, výsledkem je tuple všech aktivních tlačítek
    response = buttons_response(request)

    # počet příkladů pro jednotlivé mat. operace
    resp = get_number_of_examples()
    num_plus, num_minus, num_krat, num_deleno = resp[1], resp[2], resp[3], resp[4]

    # spuštění funkce pro určení číselného oboru get_numeric_range()

    response = buttons_response(request)

    count_plus = response[1][0]
    print(f"[1] prvek response: {count_plus}")

    addition_example = [10, 15, 7, 8, 9, 12, 113]
    math_examples = {"examples": addition_example}

    return render(request, "math_examples.html", context=math_examples)


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

        for exampl, result in zip(examples, results):

            if eval(exampl) == int(result):
                print(exampl, result, "OK")
            else:
                print(exampl, result, "NOK")

        return render(request, 'validation_math_examples.html')
