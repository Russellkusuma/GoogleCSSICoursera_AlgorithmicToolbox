# python3
import random

def max_pairwise_productFAST(numbers):
    n = len(numbers)
    x = -1
    for first in range(n):
        if numbers[first] > numbers[x] or x == -1:
            x = first
    y = -1
    for second in range(n):
        if second != x:
            if numbers[second] > numbers[y] or y == -1:
                y = second
    return numbers[x] * numbers[y]

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_productFAST(input_numbers))

##if __name__ == '__main__':
##    while True:
##        n = random.randint(2,5)
##        arr = []
##        for j in range(n):
##            arr.append(random.randint(1,10))
##        print(arr)
##        res1 = max_pairwise_product(arr)
##        res2 = max_pairwise_productFAST(arr)
##        if res1 != res2:
##            print('Wrong answer: ' + str(res1) + ' ' + str(res2))
##            break
##            pass 
##        else:
##            print('OK')
##            pass
        
