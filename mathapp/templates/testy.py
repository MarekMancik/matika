my_list = ["OK", "NOK", "OK", "OK", "NOK"]

for item in my_list:
    if "NOK" in item:
        print("NOK - příklad je v pořádku")
    elif "OK" in item:
        print("OK - příklad je špatně")