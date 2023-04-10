import sys
input = sys.stdin.readline

# 4548ms
def solution(CMD, arr):
    r_state = 1
    for i in CMD:
        if i == 'R':
            r_state *= -1
        
        elif i == 'D':
            if not arr:
                return 'error'
            
            if r_state == 1:
                arr.pop(0)
            elif r_state == -1:
                arr.pop()
    
    return str(arr[::r_state]).replace(" ", "")

T = int(input())
for i in range(T):
    CMD = input()
    input()
    arr = eval(input())
    print(solution(CMD, arr))
    

########################################################
# 108ms
import sys
input = sys.stdin.readline

def solution(CMD, length, arr):
    r_state = 1
    arr = arr.strip('[]\n').split(',')
    a, b = 0, length
    
    for i in CMD:
        if i == 'R':
            r_state *= -1
        elif i == 'D':
            if r_state == 1:
                a+=1
            elif r_state == -1:
                b-=1
            if a > b:
                return 'error'
    
    if r_state == 1:
        return f'[{",".join(arr[a:b])}]'
    elif r_state == -1:
        if a == 0:
            return f'[{",".join(arr[b-1::-1])}]'
        else:
            return f'[{",".join(arr[b-1:a-1:-1])}]'

T = int(input())
for i in range(T):
    CMD = input()
    length = int(input())
    arr = input()
    print(solution(CMD, length, arr))