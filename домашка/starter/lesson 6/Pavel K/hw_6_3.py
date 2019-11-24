import functools
@functools.lru_cache(maxsize=None)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(int(input('put number Fibonacci'))))
