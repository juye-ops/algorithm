from collections import deque
mapping = {'[': ']', '{': '}', '(': ')'}

def is_correct(s):
    stack = []
    try:
        for i in s:
            if stack and (mapping[stack[-1]] == i):
                stack.pop()
            else:
                stack.append(i)
        return not bool(stack)
    except:
        return False

def solution(s):
    answer = 0
    s = deque(s)
    for i in range(len(s)):
        answer += is_correct(s)
        s.rotate(1)

    return answer