import numpy as np
import sys
import math as mx

def sigmoid(inX) :
    return 1.0 / (1 + np.exp(-inX))

def sgn(x) :
    if mx.fabs(x) < 1e-6 :
        return 0
    elif x > 0 :
        return 1
    else :
        return -1

class FTRL :
    z = []
    N = []
    g = []
    o = []
    w = []
    n = 0
    a = 0
    b = 0
    l1 = 0
    l2 = 0
    
    def __init__(self, _n, _a, _b, _l1, _l2) :
        self.n = _n
        self.z = [0] * self.n
        self.N = [0] * self.n
        self.g = [0] * self.n
        self.o = [0] * self.n
        self.w = [0] * self.n
        self.a = _a
        self.b = _b
        self.l1 = _l1
        self.l2 = _l2

    
    def insert(self, _x, _y) :
        x = np.mat(_x)
        y = np.mat(_y).transpose()
        m = np.shape(x)[0]
        for t in range(m) :
            I = []
            for i in range(self.n) :
                if mx.fabs(x[t,i]) > 1e-6 :  
                    I.append(i)                                                                       
            for i in I :                                                                                     
                if mx.fabs(self.z[i]) <= self.l1 :                                                                 
                    self.w[i] = 0                                                                         
                else :                        
                    self.w[i] = -float((self.z[i] - sgn(self.z[i]) * self.l1) / ((self.b + mx.sqrt(self.N[i])) / self.a + self.l2)) 
            p = float(sigmoid(np.mat(x[t]) * np.mat(self.w).transpose())[0,0])                                             
            for i in I :
                self.g[i] = (p - y[t]) * x[t,i]
                self.o[i] = (mx.sqrt(self.N[i] + self.g[i] * self.g[i]) - mx.sqrt(self.N[i])) / self.a
                self.z[i] = self.z[i] + self.g[i] - self.o[i] * self.w[i]
                self.N[i] = self.N[i] + self.g[i] * self.g[i]

    def calc(self, _x) :
        return float(sigmoid(np.mat(x) * np.mat(self.w).transpose())[0, 0])
if __name__ == "__main__" : 
    f = FTRL(3, 1, 1, 0.5, 0.5)
    f.insert([[1,1,1],[1,1,2],[0,1,0],[-1,3,-1]],[1,1,0,0])
    while True :
        x = map(int, raw_input().split())
        print f.calc(x)
