# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for i in range(2,n+1):
        x = (previous + current) % 10
        previous = current
        current = x
    return current


n = int(input())
print(get_fibonacci_last_digit_naive(n))
