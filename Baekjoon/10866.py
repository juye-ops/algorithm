import sys
from collections import deque

def solution(N, reqs):
    funcs = {
        "push_front": lambda q, x: q.appendleft(x),
        "push_back": lambda q, x: q.append(x),
        "pop_front": lambda q: print(q.popleft() if q else -1),
        "pop_back": lambda q: print(q.pop() if q else -1),
        "size": lambda q: print(len(q)),
        "empty": lambda q: print(int(not bool(q))),
        "front": lambda q: print(q[0] if q else -1),
        "back": lambda q: print(q[-1] if q else -1)
    }
    
    q = deque()
    for req in reqs:
        req = req.split()
        funcs[req[0]](q, *req[1:])
        
input = sys.stdin.readline
N = int(input())
reqs = [input() for _ in range(N)]
solution(N, reqs)