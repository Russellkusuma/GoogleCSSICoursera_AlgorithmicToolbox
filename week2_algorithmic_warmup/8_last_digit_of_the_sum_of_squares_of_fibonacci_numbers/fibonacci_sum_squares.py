# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def pisano_period(m):
    previous = 1
    current = 1
    result = 1
    while not (previous == 0 and current == 1):
        x = (previous + current) % m
        previous = current
        current = x
        result += 1
    return result

def get_fibonacci_pisano_method(n,m):
    remainder = (n%pisano_period(m))
    if remainder <= 1:
        return remainder
    previous = 0
    current  = 1
    for i in range(2,remainder+1):
        x = (previous + current) % m
        previous = current
        current = x
    return current

def fibonacci_sum_squared_pisano_method(n):
    return ((get_fibonacci_pisano_method(n, 10) * get_fibonacci_pisano_method(n+1, 10))%10)

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squared_pisano_method(n))
