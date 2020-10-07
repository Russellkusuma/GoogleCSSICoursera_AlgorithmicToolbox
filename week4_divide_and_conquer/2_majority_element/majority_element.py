# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    majorityIndex = 0
    x = 1

    #Find majority
    for i in range(1,right):
        if a[i] == a[majorityIndex]:
            x+=1
        else:
            x-=1
        if x == 0:
            majorityIndex = i
            x = 1
    x = 0

    #Check majority
    for i in range(right):
        if a[i] == a[majorityIndex]:
            x += 1
    if x>(right//2):
        return a[majorityIndex]
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
