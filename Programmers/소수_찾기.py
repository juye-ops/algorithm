def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0: return False
    return True

def solution(n):
    return len(list(filter(lambda x: is_prime(x), range(2, n+1))))