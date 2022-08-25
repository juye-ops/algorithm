from math import gcd

def solution(w,h):
    GCD = gcd(w, h)
    w1, h1 = w//GCD, h//GCD
    return w * h - ((w1 + h1 - 1) * GCD)