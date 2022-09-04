from itertools import combinations

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:return False
    return True

def solution(nums):
    return sum(list(map(is_prime, map(lambda x: sum(x),combinations(nums, 3)))))