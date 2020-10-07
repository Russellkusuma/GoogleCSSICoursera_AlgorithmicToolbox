# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

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

def get_fibonacci_sum_pisano_method(n):
    remainder = (n%pisano_period(10))
    if (remainder <= 1):
        return remainder
    previous = 0
    current  = 1
    sum = 1
    for i in range(2,remainder+1):
        previous, current = current, previous + current
        sum += current
    return sum%10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_sum_pisano_method(n))
