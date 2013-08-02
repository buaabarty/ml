import sys
import math
import matplotlib.pyplot as plt
import matplotlib.lines as lines

if __name__ == "__main__" :
    n = 100000
    width = float(sys.argv[2])
    i = 0.
    x = []
    y = []
    tot = 0
    while i <= 1 :
        tp = 0; fp = 0; fn = 0; tn = 0
        fin = open(sys.argv[1])
        while True :
            line = fin.readline()
            if line :
                a, b = map(float, line.split())
                if math.fabs(b-1.0) < 1e-3 :
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
        x.append(tp * 1. / (tp + fp))
        y.append(tp * 1. / (tp + fn))
        i = i + width
        tot = tot + 1
#    x.append(1)
#    y.append(0)
    plt.plot(x, y)
    plt.axis([0,1,0,1])
    plt.xlabel('precision')
    plt.ylabel('recall')
    plt.title('PR curve')
    plt.show()
