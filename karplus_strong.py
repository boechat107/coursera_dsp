# ========================================================================================= 
# Author: Andre A. Boechat
# File: karplus_strong.py
# Date: March 01, 2013, 06:53:31 PM
# Description: Implementation of the Karplus-Strong algorithm for the Coursera's
# Digital Signal Processing course. 
# 
# Reference: 
# https://www.coursera.org/course/dsp
# ========================================================================================= 
import pylab as pl
from scipy import *
import functools as ft
import time

def karplus_strong(x, alpha, D):
    M = len(x)
    y = zeros(M*D)
    y[0:M] = x
    for idx in range(M, M*D):
        y[idx] = alpha * y[idx - M]
    return y

def ks_mat(x, alpha, D):
    M = len(x)
    alpha_mat = array([alpha ** arange(D)]).repeat(M, axis=0).transpose()
    x_mat = array([x]).repeat(D, axis=0)
    y_mat = alpha_mat * x_mat
    return y_mat.reshape(y_mat.size)


if __name__ == "__main__":
    x = randn(100)
    alpha = .9
    D = 10
    now = time.time()
    y1 = karplus_strong(x, alpha, D)
    print(time.time() - now)
    ## Matrix implementation
    now = time.time()
    y2 = ks_mat(x, alpha, D)
    print(time.time() - now)
    pl.subplot(1,2,1)
    pl.stem(range(0, len(y1)), y1)
    pl.subplot(1,2,2)
    pl.stem(range(0, len(y2)), y2)
    pl.show()
    
