def solution(A, B, C):
    if B == 1:
        return A%C
  
    tmp = solution(A,B//2, C)
    if B % 2 ==0:
        return (tmp * tmp) % C
    else:
        return (tmp  * tmp * A) % C

A, B, C = map(int,input().split())         
print(solution(A, B, C))