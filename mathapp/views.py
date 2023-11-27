from django.shortcuts import render, HttpResponse
from mathapp.math_models import MathCase


# Create your views here.
def buttons_response(request):
    math_operation_buttons = request.POST.getlist('button')
    number_of_examples = request.POST.getlist('select_button_plus')
    numeric_range = request.POST.getlist('button_2')


    print(f"Byla aktivována tato tlačítka: {math_operation_buttons}")
    print(f"počet příkladů: {number_of_examples}")
    print(f"další tlačítka:{numeric_range}")

    # 1. set number of examples translate from list to int
    num_examples = int(number_of_examples[0])
    # 2. set numeric_range

    for every_range in numeric_range:
        if every_range == "range_0-10":
            range_low = 0
            range_high = 10
        elif every_range == "range_0-20":
            range_low = 0
            range_high = 20

    # 3. look at the type of math operations
    for math_operation in math_operation_buttons:
        if math_operation == "plus":
            MathCase.addition(count=num_examples, numeric_range_low=range_low , numeric_range_high=range_high)
        elif math_operation == "minus":
            pass
        elif math_operation == "krat":
            pass
        elif math_operation == "deleno":
            pass


    # return math_operation_buttons, number_of_examples, numeric_range
    return HttpResponse(f"Data byla přijata! {math_operation_buttons}, {number_of_examples}, {numeric_range}")





def generate_math_examples(request):
    # receive a requirement regarding generating of math examples - typ, range, count
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

        for exampl, result in zip(examples, results):

            if eval(exampl) == int(result):
                print(exampl, result, "OK")
            else:
                print(exampl, result, "NOK")

        return render(request, 'validation_math_examples.html')



