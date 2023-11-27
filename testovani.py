list_typ_example = ["plus", "minus"]
list_range_of_value = ["range_20-100"]
count = 20
list_range_of_type = [50, 50]

# vytvořím speciální list pro každou matematickou operaci, musí obsahovat danou operaci, rozsah, počet příkladů
list_case_plus = []
list_case_minus = []
list_case_krat = []
list_case_deleno = []

# potřebuju vybrat všechny typy příkladů tzn. +/-/x/:
for type_example in list_typ_example:
    if type_example == "plus":
        list_case_plus.append(type_example)
    elif type_example == "minus":
        list_case_minus.append(type_example)
    elif type_example == "krat":
        list_case_krat.append(type_example)
    elif type_example == "deleno":
        list_case_deleno.append(type_example)

# tady musím rozhodnout, které listy jsou prázdné, tak je dál nebudu používat.

print(list_case_plus, list_case_minus, list_case_krat,
      list_case_deleno)  # výpis obsahu jednotlivých listů generující příklad


def range_value_for_examples(range_example):
    for range_value in range_example:
        if range_value == "range_0-10":
            yield 0, 10
        elif range_value == "range_0-20":
            yield 0, 20
        elif range_value == "range_20-100":
            yield 20, 100


print(range_value_for_examples)
to_tuple = range_value_for_examples(list_range_of_value)
first_value = next(to_tuple)
print(f"původní yield: {to_tuple}")
print(f"Původní list: {list_case_plus}")
print(f"tuple rozsahu počítání: {first_value}")

extend_list = list_case_plus.append('test')
print(f"přičtený list: {extend_list}")

# if len(list_case_plus) > 0:
#     for range_value in list_range_of_value:
#
#         if range_value == "range_0-10":
#             list_case_plus.extend()
#
#         if range_value == "range_0-10":
#             list_case_minus.append(0)
#             list_case_minus.append(20)


# potřebuju vybrat číselný rozsah 0-10, 0-20, 20-100

# potřebuju zjistit kolik příkladů vygenerovat 5, 10, 15, 20, 25

# potřebuju zjistit poměr mezi danými příklady, pokud je třeba +/-, x/:
