# 왼쪽 순차 탐색
def to_left(queue, idx, t):
    cnt = 0
    while queue[idx] != t:
        idx-=1
        cnt+=1
        if idx < 0:
            idx = len(queue) - 1
            
    return idx, cnt

# 오른쪽 순차 탐색
def to_right(queue, idx, t):
    cnt = 0
    while queue[idx] != t:
        idx+=1
        cnt+=1
        if idx >= len(queue):
            idx = 0
            
    return idx, cnt


N, M = map(int, input().split())

queue = list(range(1, N+1))
target = list(map(int, input().split()))

idx = 0

answer = 0
while target:
    if idx < 0: idx = len(queue) - 1
    elif idx >= len(queue): idx = 0
    
    # 양쪽 순차탐색
    idx1, cnt1 = to_left(queue, idx, target[0])
    idx2, cnt2 = to_right(queue, idx, target[0])
    
    # 순차 탐색 결과 중 최소 이동으로 얻은 값을 Greedy 하게 선정
    answer += min(cnt1, cnt2)
    
    # idx 재수립 (idx1 == idx2)
    idx = idx1  # == idx2
    
    queue.pop(idx)
    target.pop(0)
    
print(answer)