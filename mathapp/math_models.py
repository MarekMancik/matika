# created math model for every math function.

# I have to create math model for every case - +, -, x, :, generated random number in range 0-10,0-20,10-100,100-1000
import random


class Addition:
    i = 1
    @staticmethod
    def case(math_operation, numeric_range_low, numeric_range_high):
        for i in range(10):
            a = random.randint(numeric_range_low, numeric_range_high)
            b = random.randint(numeric_range_low, numeric_range_high)

            if (a + b) < numeric_range_high:

                return f"{a}{math_operation}{b} ="

        return None


first_example = Addition.case(math_operation="+", numeric_range_low=0, numeric_range_high=20)
print(first_example)
