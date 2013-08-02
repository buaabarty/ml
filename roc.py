import sys
import math
import matplotlib.pyplot as plt

if __name__ == "__main__" :
    n = 100000
    width = float(sys.argv[2])
    i = 0.
    x = []
    y = []
    tot = 1
    while i <= 1 :
        tp = 0; fp = 0; fn = 0; tn = 0; p = 0
        fin = open(sys.argv[1])
        while True :
            line = fin.readline()
            if line :
                a, b = map(float, line.split())
                if math.fabs(b-1.0) < 1e-3 :
                    p = p + 1
                    if a < i :
                        fn = fn + 1
                    else :
                        tp = tp + 1
                else :
                    if a < i :
                        tn = tn + 1
                    else :
                        fp = fp + 1
            else :
                break
        x.append(tp)
        y.append(fp)
        i = i + width
        tot = tot + 1
    x.append(0)
    y.append(0)
    for i in range(tot) :
        x[i] = x[i] * 1. / p
        y[i] = y[i] / 100000.
    plt.plot(x, y)
    plt.axis([0,1,0,1])
    plt.xlabel('TPR')
    plt.ylabel('FPR')
    plt.title('ROC curve')
    plt.show()
