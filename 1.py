

def caching_fibonacci():
    """
    function to cache fibonacci function results
    Creates and return the function fibonacci.
    
    It adds every result calculation into dictionary cashe,
    in format {n: Fibonacci(n)}, where key is fibonacci index and 
    value is calculated Fibonacci number for that index

    Using caching improves the speed of computation and
    avoids unnecesary recursive calls.

    By doing caching we achieve that function needs to calculate 
    only fibonacci numbers in the range 
    (furthest calculated fibonacci number, needed fibonacci number)
    """
    cache = {}
    def fibonacci(n: int) -> int:
        """
        calculates Nth Fibonacci number 
        input: n: necessary index
        output: fibonacci number for the n index

        if the Fibonacci number is already calculated (is included in the cache dict),
        it does not calculate the number, just returns saved fibonacci number.
        Otherwise, recursively computes Fibonacci number recursively, down to 
        the largest previously calculated number
        """
        #basic cases for the fibonacci numbers
        if n <= 0:
            return 0
        if n ==1:
            return 1
        # check if the result was previously calculated to avoid unnecessary computations
        if n in cache:
            return cache[n]
        # calculate fibonacci number recursevly
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci

if __name__ == "__main__":
    # Отримуємо функцію fibonacci
    fib = caching_fibonacci()

    # Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
    # first calculation calculates all the numbers up to 10
    print(fib(10))  # Виведе 55
    # second calculation does not need to do extra computation, and calculates
    # only numbers in the range  from 10 to 15
    print(fib(15))  # Виведе 610

    

        
