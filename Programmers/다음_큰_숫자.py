def solution(n):
    if n == 0: return 0
    if n == 1: return 2
    binary = bin(n).lstrip("0b")
    i = binary.rfind('1')

    binary = list(binary)
    cnt = binary.count("1")

    swap = 0
    while binary[i] == "1":
        binary[i] = "0"
        i -= 1
    if i == -1:
        binary.insert(0, "1")

    binary[i]="1"

    i = -1
    while binary.count("1") != cnt:
        binary[i]="1"
        i-=1
    print(binary)
    binary = "0b" + "".join(binary)

    return int(binary, 2)