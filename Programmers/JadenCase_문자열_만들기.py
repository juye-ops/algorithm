def solution(s):
    return " ".join([(i[0].upper() + i[1:].lower()) if i != '' else "" for i in s.split(' ')])