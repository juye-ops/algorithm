def solution(word):
    answer = 0
    
    alpha = 'AEIOU'
    gap = [5*(5*(5*(1*5+1)+1)+1)+1, 5*(5*(1*5+1)+1)+1, 5*(1*5+1)+1, 1*5+1, 1]
    
    for i, x in enumerate(word):
        answer += (alpha.index(x) * gap[i])+1
    
    return answer

# gap[i-1] = gap[i] * 5 + 1