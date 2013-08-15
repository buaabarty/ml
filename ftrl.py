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

def ftrl(dataMatIn, classLabels) :
  x = np.mat(dataMatIn)
  y = np.mat(classLabels).transpose()
  m, n = np.shape(x)
  z = [0] * n
  N = [0] * n
  g = [0] * n
  o = [0] * n
  w = [0] * n
  a = 1.
  b = 1.
  l1 = 0.5
  l2 = 0.5
  for t in range(m) :
         I = []
         for i in range(n) :
           if mx.fabs(x[t,i]) > 1e-6 :                                                             
                   I.append(i)                                                                       
         for i in I :                                                                                     
           if mx.fabs(z[i]) <= l1 :                                                                 
                   w[i] = 0                                                                         
           else :                        
                   w[i] = -float((z[i] - sgn(z[i]) * l1) / ((b + mx.sqrt(N[i])) / a + l2)) 
         p = float(sigmoid(np.mat(x[t]) * np.mat(w).transpose())[0,0])                                             
         for i in I :
           g[i] = (p - y[t]) * x[t,i]
           o[i] = (mx.sqrt(N[i] + g[i] * g[i]) - mx.sqrt(N[i])) / a
           z[i] = z[i] + g[i] - o[i] * w[i]
           N[i] = N[i] + g[i] * g[i]
  return w

if __name__ == "__main__" :                                                                                      
  w = ftrl([[1,1,1],[1,1,2],[0,1,0],[-1,3,-1]],[1,1,0,0])     
  while True :
         x = map(int, raw_input().split())
         p = float(sigmoid(np.mat(x) * np.mat(w).transpose())[0,0])
         print p
