from collections import deque

def solution(N, M, knows, participants):
    answer = set()
    q = deque()
    
    for i in knows:
        for j in participants[i]:
            q.append(j)
            
    while q:
        now = q.popleft()
        answer.add(now)
        
        for i in participants:
            if i in knows:
                continue
            if now in participants[i]:
                knows.add(i)
                for j in participants[i]:
                    q.append(j)
    
    return M - len(answer)
                
        
    


N, M = map(int, input().split())
knows = set(list(map(int, input().split()))[1:])
participants = {x: [] for x in range(1, N+1)}
for i in range(M):
    for j in list(map(int, input().split()))[1:]:
        participants[j].append(i)

print(solution(N, M, knows, participants))

# {1: [0, 4], 2: [1], 3: [2], 4: [3, 4]}