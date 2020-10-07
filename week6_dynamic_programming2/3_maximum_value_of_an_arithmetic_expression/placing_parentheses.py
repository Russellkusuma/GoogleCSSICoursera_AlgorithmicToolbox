# Uses python3
import sys
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    for i in range(len(digits)):
        max[i][i] = digits[i]
        min[i][i] = digits[i]

    for s in range(0, len(digits)):
        for i in range(0, len(digits) - s - 1):
            j = i + s + 1
            min_value, max_value = min_max_value(i, j)
            max[i][j] = maxValue
            min[i][j] = minValue

def min_max_value(i, j):
    minValue = (sys.maxsize)
    maxValue = -(sys.maxsize)
    for k in range(i, j):
        a = evalt(max[i][k], max[k+1][j], ops[k])
        b = evalt(max[i][k], min[k+1][j], ops[k])
        c = evalt(min[i][k], max[k+1][j], ops[k])
        d = evalt(min[i][k], min[k+1][j], ops[k])
        minValue = min(minValue, a, b, c, d)
        maxValue = max(maxValue, a, b, c, d)
    return minValue, maxValue


if __name__ == "__main__":
    dataset = input()
    digits = list(map(int, dataset[0::2]))
    ops = list(dataset[1::2])
    min = [[0 for x in range(len(digits))] for y in range(len(digits))]
    max = [[0 for x in range(len(digits))] for y in range(len(digits))]
    get_maximum_value(dataset)
    print(max[0][len(digits) - 1])
if __name__ == "__main__":
    print(get_maximum_value(input()))
