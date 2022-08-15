def solution(operations):
    q = []
    
    for i in operations:
        oper, num = i.split()
        num = int(num)
        if oper == "D" and q:
            if num == 1:
                q.remove(max(q))
            elif num == -1:
                q.remove(min(q))
        elif oper == "I":
              q.append(num)  
        print(q)
    
    return [0, 0] if not q else [max(q), min(q)]