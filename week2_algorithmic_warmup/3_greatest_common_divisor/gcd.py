# Uses python3

def gcd_euclid(a, b):
    if b == 0:
        return a
    if a == b:
        return a
    x = a % b
    return gcd_euclid(b,x)

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd_euclid(a, b))
