# Uses python3
import sys
import math

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def dynamicSequence(n):
    if n == 1:
        return [1]
    operations = minimumOperations(n)
    sequence = []
    while n >= 1:
        sequence.append(n)
        if (n%3!=0 and n%2!=0):
            n-=1
        elif n%3==0 and n%2==0:
            n = n//3
        elif n%2==0:
            if operations[n-1]<operations[n//2]:
                n-=1
            else:
                n = n//2
        elif n%3==0:
            if operations[n-1]<operations[n//3]:
                n-=1
            else:
                n = n//3
    return reversed(sequence)
            
def minimumOperations(n):
    result = []
    for i in range(0,n+1):
        result.append(0)
    for i in range(2,n+1):
        min1 = result[i-1]
        min2 = math.inf
        min3 = math.inf
        if i % 2 == 0:
            min2 = result[int(i/2)]
        if i % 3 == 0:
            min3 = result[int(i/3)]
        minOp = min(min1, min2, min3)
        result[i] = (minOp+1)
    return result

input = sys.stdin.read()
n = int(input)
sequence = list(dynamicSequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
