import sys
import math
import matplotlib.pyplot as plt

if __name__ == "__main__" :
    n = 100000
    fin = open(sys.argv[1])
    x = []
    y = []
    while True :
        line = fin.readline()
        if line :
            a, b = map(float, line.split())
            if math.fabs(b - 1.0) < 1e-3 :
                x.append(a)
            else :
                y.append(a)
        else :
            break
    x.sort()
    y.sort()
    sx = len(x)
    sy = len(y)
    j = 0
    tot = 0
    for i in range(sx) :
        while j < sy and x[i] > y[j] :
            j = j + 1
        tot += j
    tot = tot * 1. / (sx * sy)
    print tot
