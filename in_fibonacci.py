

"""find the fibonacci number by position"""


def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))


"""check if the number is in fibonacci"""


def check_in_fibonacci(number: int) -> str:
    if number < 0:
        return "Números negativos não pertencem à sequência de Fibonacci."

    position = 0
    while True:
        fibonacci_number = fibonacci(position)
        if fibonacci_number == number:
            return f"O número {number} percente à sequência Fibonacci."
        elif fibonacci_number > number:
            return f"O número {number} não percente à sequência Fibonacci"
        position += 1


input_number = int(input(
    "Informe um número para procurar na sequência de Fibonacci: "))
print(check_in_fibonacci(input_number))
