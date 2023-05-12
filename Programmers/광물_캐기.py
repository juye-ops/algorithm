from collections import deque


def solution(picks, minerals):
    answer = float("inf")
    
    cost = [
        {
            "diamond": 1,
            "iron": 1,
            "stone": 1,
        },
        {
            "diamond": 5,
            "iron": 1,
            "stone": 1,
        },
        {
            "diamond": 25,
            "iron": 5,
            "stone": 1,
        }   
    ]
    
    q = deque()
    now = (picks, minerals, 0)
    
    q.append(now)
    
    while q:
        pick, mineral, n = q.popleft()
        
        if not mineral or not any(pick):
            answer = min(answer, n)
            continue
        
        for i in range(3):
            n_pick = pick[:]
            n_mineral = mineral[:]
            if not n_pick[i]:
                continue
            n_pick[i]-=1
            v = 0
            for x in n_mineral[:5]:
                v += cost[i][x]
            
            q.append((n_pick, n_mineral[5:], n+v))
    return answer
