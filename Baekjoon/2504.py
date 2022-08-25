def solution(string):
    stack = []
    answer = ""
    for i in string:
        if i == "(":
            answer+="2*("
            stack.append(i)
        if i == "[":
            answer+="3*("
            stack.append(i)
        if i == ")":
            if stack and stack[-1] == "(":
                answer += "1)+"
                stack.pop()
            else: return 0
        if i == "]":
            if stack and stack[-1] == "[":
                answer += "1)+"
                stack.pop()
            else: return 0
    if stack: return 0
    return (eval(answer.replace(")+1", ")")[:-1]))

print(solution(input()))