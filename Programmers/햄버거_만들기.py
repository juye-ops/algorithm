def solution(ingredient):
    answer = 0
    
    stack = ingredient[:3]
    
    for i in ingredient[3:]:
        stack.append(i)
        if stack[-4:] == [1,2,3,1]:
            for i in range(4):
                stack.pop()
            answer+=1
    
    
    return answer