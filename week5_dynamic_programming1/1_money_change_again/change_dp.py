# Uses python3
import sys
import math

def get_change(m):
    coinType = [1,3,4]
    minCoins = [0]
    for i in range(1,m+1):
        minCoins += [math.inf]*m
        for t in coinType:
            if i>=t:
                coins = minCoins[i-t]+1
                if coins < minCoins[i]:
                    minCoins[i] = coins
    return minCoins[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
