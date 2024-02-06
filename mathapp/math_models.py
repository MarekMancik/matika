# created math model for every math function.

# I have to create math model for every case - +, -, x, :, generated random number in range 0-10,0-20,10-100,100-1000
import random
from typing import List

my_numbers = [
    [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9],
    [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9],
    [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9],
    [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9],
    [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9],
    [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [6, 8], [6, 9],
    [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7], [7, 8], [7, 9],
    [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [8, 8], [8, 9],
    [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8], [9, 9],
    ]




class MathCase:
    @staticmethod
    def addition(count: int, numeric_range_low: int, numeric_range_high: int) -> list[str]:
        examples = []
        while len(examples) < count:
            a = random.randint(numeric_range_low, numeric_range_high)
            b = random.randint(numeric_range_low, numeric_range_high)
            if a + b <= numeric_range_high:
                examples.append(f"{a}+{b}")

        return examples

    @staticmethod
    def substraction(count: int, numeric_range_low: int, numeric_range_high: int):
        examples = []
        while len(examples) < count:
            a = random.randint(numeric_range_low, numeric_range_high)
            b = random.randint(numeric_range_low, numeric_range_high)
            if a > b:
                examples.append(f"{a}-{b}")
            else:
                examples.append(f"{b}-{a}")
        return examples


    @staticmethod
    def multiplication(count: int, numeric_range_low: int, numeric_range_high: int):
        if numeric_range_low == 0 and numeric_range_high == 100:
            examples = []
            numbers = random.sample(my_numbers, count)
            for one_numbers in numbers:
                examples.append(f"{one_numbers[0]}x{one_numbers[1]}")

            return examples

    @staticmethod
    def division(count: int, numeric_range_low: int, numeric_range_high: int):
        if numeric_range_low == 0 and numeric_range_high == 100:
            examples = []
            numbers = random.sample(my_numbers, count)
            for one_number in numbers:
                dividing_number = one_number[0] * one_number[1]
                examples.append(f"{dividing_number}:{one_number[1]}")
            return examples

    @staticmethod
    def addition_50(count: int, numeric_range_low: int, numeric_range_high: int):
        examples = []
        while len(examples) < count:
            a = random.randint(numeric_range_low, numeric_range_high)
            b = random.randint(1, 10)
            if a + b <= 50:
                examples.append(f"{a}+{b}")

        return examples

    @staticmethod
    def substraction_50(count: int, numeric_range_low: int, numeric_range_high: int):
        examples = []
        while len(examples) < count:
            a = random.randint(numeric_range_low, numeric_range_high)
            b = random.randint(1, 10)
            examples.append(a - b)
        return examples

# for i in range(10):
#     add_examples = MathCase.addition(numeric_range_low=0, numeric_range_high=20)
#     i += 1
#     print(add_examples)
#
# for i in range(10):
#     sub_examples = MathCase.substraction(numeric_range_low=0, numeric_range_high=20)
#     i += 1
#     print(sub_examples)

# for i in range(10):
#     multi_examples = MathCase.multiplication(count=10, numeric_range_low=0, numeric_range_high=100)
#     i += 1
#     print(multi_examples)

# for i in range(10):
#     divi_examples = MathCase.division(count=10, numeric_range_low=0, numeric_range_high=100)
#     i += 1
#     print(divi_examples)

