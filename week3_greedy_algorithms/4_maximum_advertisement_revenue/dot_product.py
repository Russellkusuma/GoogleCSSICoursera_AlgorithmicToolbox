#Uses python3

import sys

def get_max_index(array):
    biggestIndex = 0
    for i in range(len(array)):
        if array[biggestIndex] < array[i]:
            biggestIndex = i
    return biggestIndex

def max_dot_product(a, b):
    #write your code here
    res = 0
    for i in range(len(a)):
        aMax = get_max_index(a)
        bMax = get_max_index(b)
        res += (a[aMax] * b[bMax])
        a.pop(aMax)
        b.pop(bMax)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
