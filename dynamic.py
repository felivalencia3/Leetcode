# Fibonacci numbers
# Traditional recursive fib

def trad_fib(n):
    if n <= 1:
        return 1
    return trad_fib(n - 1) + trad_fib(n - 2)


print(trad_fib(5))
