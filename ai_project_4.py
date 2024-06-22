# -*- coding: utf-8 -*-
"""mycaptain_ai_project_4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/124MUo0UZLdpUEvIAsFbDWb14rMaPUn-n
"""

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
def fibonacci_iterative(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
n = 15
fib_sequence_recursive = [fibonacci_recursive(i) for i in range(n)]
fib_sequence_iterative = fibonacci_iterative(n)
print(f"First {n} Fibonacci numbers (recursive): {fib_sequence_recursive}")
print(f"First {n} Fibonacci numbers (iterative): {fib_sequence_iterative}")