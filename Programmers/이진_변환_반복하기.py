def solution(s):
    a = b = 0
    while s != "1":
        print(s)
        zero_count = s.count("0")
        s = s.replace("0", "")
        b += zero_count
        s = bin(len(s)).lstrip("0b")
        a+=1
    return [a, b]