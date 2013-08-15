# logistic regression with gradient descent and line search
# Barty

import sys
import math
import numpy

def sigmoid(x) :
    return 1.0 / (1 + numpy.exp(-x))

def L(x, y, weights) :
    m, n = numpy.shape(x)
    xx = x * weights
    ret = 0
    for i in range(m) :
        ret = ret + xx[i][0] * y[i][0] - math.log(1 + math.exp(xx[i][0]))
    return ret


def gd(x, y) :
    m, n = numpy.shape(x)
    times = 0
    weights = numpy.ones((n, 1))
    lastres = math.exp(L(x, y, weights))
    while True :
        tmp = x * weights
        h = sigmoid(x * weights)
        error = (h - y)
        tmp = x.T * error
        left = 0.; right = 1.; midleft = 0.; midright = 0.
        while right - left > 1e-6 :
            midleft = (right - left) / 3. + left
            midright = (right - left) * 2. / 3. + left
            if L(x, y, weights - midleft * x.T * error / m) < L(x, y, weights - midright * x.T * error / m) :
                right = midright
            else :
                left = midleft
        weights = weights - left * x.T * error / m
        nowres = math.exp(L(x, y, weights))
        if math.fabs(nowres - lastres) < 1e-10 :
            break
        lastres = nowres
    return weights


if __name__ == "__main__" :
    x = numpy.mat([[1,2,3],[1,3,4],[1,5,6]])
    y = numpy.mat([[0,1,1]]).T
    theta = gd(x, y)
    print math.exp(L(x, y, theta))
    a = [1, -100000, -100000]
    print sigmoid(numpy.mat(a) * theta)
    a = [1, 8, 9]
    print sigmoid(numpy.mat(a) * theta)
