import math

def solution(n, m):
    answer = [math.gcd(n, m), (n*m)//math.gcd(n, m)]
            
    return answer