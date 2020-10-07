# Uses python3
def edit_distance(s, t):
    arr=[[0 for x in range(len(s)+1)] for y in range(len(t)+1)]
    for x in range(len(s)+1):
        arr[0][x] = x
    for y in range(len(t)+1):
        arr[y][0] = y
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            insert = arr[j-1][i]+1
            delete = arr[j][i-1]+1
            match = arr[j-1][i-1]
            mismatch = arr[j-1][i-1]+1
            if s[i-1] == t[j-1]:
                arr[j][i] = min(insert,delete,match)
            else:
                arr[j][i] = min(insert,delete,mismatch)
    return arr[len(t)][len(s)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
