# Uses python3
def calc_fib(n):
    a = [0 for x in range(n+1)]
    a[0] = 0
    if n != 0:
        a[1] = 1
    for i in range(2,n+1):
        a[i] = a[i-1] + a[i-2]
    return a[n]

n = int(input())
print(calc_fib(n))
