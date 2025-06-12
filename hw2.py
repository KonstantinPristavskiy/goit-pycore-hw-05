import re
from typing import Callable, Iterator

def generator_numbers(text: str) -> Iterator[float]:
    """
    Analyses text and returns all numbers in text as generator
    Text must have all the numbers separated with spaces.
    """
    # split text into words
    words = text.split()  
    for word in words:
        try:
            # yield float number
            yield float(word)
        # if the word is not a number that can be converted using float()
        except ValueError:
            # pass the word and continue with next word
            pass


def sum_profit(text: str, func: Callable) -> float:
    """
    calcucates the sum of the profits.
    Returns sum of the generator.
    """
    return sum(func(text))

if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
