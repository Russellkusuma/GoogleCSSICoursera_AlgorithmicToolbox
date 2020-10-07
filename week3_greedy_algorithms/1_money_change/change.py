# Uses python3
import sys

def get_change(m):
    getTens = int(m/10)
    m = m%10
    getFives = int(m/5)
    m = m%5
    getOnes = int(m/1)
    return (getTens + getFives + getOnes)

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
