# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

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

def fibonacci_partial_sum_pisano_method(m, n):
    return (get_fibonacci_pisano_method(n+2, 10) + 10 - get_fibonacci_pisano_method(m+1, 10)) % 10
    
if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_pisano_method(from_, to))