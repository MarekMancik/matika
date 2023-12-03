# created math model for every math function.

# I have to create math model for every case - +, -, x, :, generated random number in range 0-10,0-20,10-100,100-1000
import random
from typing import List


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
    def multiplication(count, numeric_range_low, numeric_range_high):
        examples = []
        while len(examples) < count:
            a = random.randint(numeric_range_low, numeric_range_high/10)
            b = random.randint(numeric_range_low, numeric_range_high/10)
            if a < 10 and b < 10:
                if (a*b) != 0 and a != 1 and b != 1:
                    examples.append(f"{a}x{b}")

        return examples

    @staticmethod
    def division(count, numeric_range_low, numeric_range_high):
        while True:
            a = random.randint(numeric_range_low, numeric_range_high)
            b = random.randint(numeric_range_low, numeric_range_high/10)
            if b != 0 and a != 0 and b != 1 and a <= b*10:
                if (a % b) == 0:
                    return f"{a}:{b}="


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
#     multi_examples = MathCase.multiplication(numeric_range_low=0, numeric_range_high=100)
#     i += 1
#     print(multi_examples)

# for i in range(10):
#     divi_examples = MathCase.division(numeric_range_low=0, numeric_range_high=100)
#     i += 1
#     print(divi_examples)

