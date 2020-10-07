# Uses python3
import sys

def optimal_weight(W, w):
    result = [[0 for x in range(W+1)] for y in range(n+1)]
    for i in range(1,n+1):
        for weight in range(1,W+1):
            result[i][weight] = result[i-1][weight]
            if (w[i-1]<=weight):
                z = result[i-1][weight-w[i-1]]+w[i-1]
                if z > result[i][weight]:
                    result[i][weight] = z
    return result[n][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
