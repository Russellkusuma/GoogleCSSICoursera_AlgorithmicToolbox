# Uses python3

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for i in range(2,n+1):
        x = (previous + current) % m
        previous = current
        current = x
    return current

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


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fibonacci_pisano_method(n, m))
