import sys
import math
import matplotlib.pyplot as plt

if __name__ == "__main__" :
    n = 100000
    width = float(sys.argv[2])
    i = 0.
    x = []
    y = []
    tot = 0
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
    for i in range(tot) :
        x[i] = x[i] * 1. / p
        y[i] = y[i] / 100000.
    plt.plot(y, x)
    plt.axis([0,1.1,0,1.1])
    plt.xlabel('FPR')
    plt.ylabel('TPR')
    plt.title('ROC curve')
    plt.show()
