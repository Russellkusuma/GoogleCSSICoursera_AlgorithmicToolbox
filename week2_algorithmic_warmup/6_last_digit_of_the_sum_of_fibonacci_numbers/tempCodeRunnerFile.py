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