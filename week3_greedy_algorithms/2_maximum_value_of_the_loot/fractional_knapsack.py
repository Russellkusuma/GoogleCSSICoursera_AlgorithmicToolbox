# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    if capacity == 0:
        return 0
    while capacity > 0:
        maxValueIndex = get_max_value_per_unit(weights, values)
        if maxValueIndex >= 0:
            weightsUsed = min(capacity, weights[maxValueIndex])
            value += (weightsUsed*(values[maxValueIndex]/weights[maxValueIndex]))
            weights[maxValueIndex] -= weightsUsed
            capacity -= weightsUsed
        else:
            return value
    return value
def get_max_value_per_unit(weights, values):
    max = 0
    maxIndex = -1
    for i in range(len(weights)):
        if weights[i] > 0:
            if (max < (values[i]/weights[i])):
                maxIndex = i
                max = (values[i]/weights[i])
    return maxIndex

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
