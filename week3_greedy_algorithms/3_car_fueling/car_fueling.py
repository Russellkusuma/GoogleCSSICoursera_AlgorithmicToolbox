# python3
import sys

def compute_min_refills(distance, tank, stops):
    numRefills = 0
    currentRefill = 0
    stops.insert(0,0)
    stops.append(distance)
    while currentRefill <= (len(stops)-2):
        lastRefill = currentRefill
        while ((currentRefill <= (len(stops)-2)) and (stops[currentRefill + 1] - stops[lastRefill] <= tank)):
            currentRefill += 1
        if currentRefill == lastRefill:
            return -1
        if currentRefill <= (len(stops)-2):
            numRefills += 1
    return numRefills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
