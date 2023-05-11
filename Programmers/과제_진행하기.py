def htom(time):
    h, m = time.split(":")
    return int(h) * 60 + int(m)
    

def solution(plans):
    answer = []
    stack = []
    plans = [[p, htom(s), int(t)] for p, s, t in plans]
    plans.sort(key = lambda x: x[1])
    
    plan_se = {x[0]: x[2] for x in plans}
    
    for i in range(1, len(plans)):
        prev = plans[i-1]
        now = plans[i]
        
        plan_se[prev[0]] -= now[1] - prev[1]
        if plan_se[prev[0]] <= 0:
            answer.append(prev[0])
            
            while stack and plan_se[prev[0]] < 0:
                mini = min(-plan_se[prev[0]], plan_se[stack[-1]])
                plan_se[stack[-1]] -= mini
                plan_se[prev[0]] += mini
                if plan_se[stack[-1]] == 0:
                    answer.append(stack.pop())
        else:
            stack.append(prev[0])
    answer.append(now[0])
    while stack:
        answer.append(stack.pop())
    
    return answer