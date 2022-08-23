def solution(numbers, target):
    
    if len(numbers) == 1:
        if numbers[0] == abs(target):
            return 1
        else: return 0
    return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])