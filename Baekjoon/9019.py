#PyPy3
from collections import deque
import sys
input = sys.stdin.readline

func = {
    "D": lambda x: x*2 % 10000,
    "S": lambda x: (x-1) % 10000,
    "L": lambda x: (x*10 + (x//1000)) % 10000,
    "R": lambda x: (x//10 + (x % 10)*1000)%10000
}

def solution(query, target):
    q = deque()
    visited = [False] * 10000

    now = (query, "")
    q.append(now)
    
    while q:
        query, answer = q.popleft()

        if query == target:
            return answer
        
        for f in func:
            a = func[f](query)
            if not visited[a]:
                visited[int(a)] = True
                q.append((a, answer+f))



T = int(input())
for _ in range(T):
    query, target = map(int, input().split())
    print(solution(query, target))