def solution(n, k):
    jinsu = ""
    answer = 0
    while n:
        n, a = divmod(n,k)
        jinsu+=str(a)
    jinsu = jinsu[::-1]
    jinsu+="0"
    sosulist = []
    i = 0
    string = ""
    for i in jinsu:
        if i != "0":
            string+=i

        else:
            if string:
                sosulist.append(int(string))
            string = ""

    for i in sosulist:
        trigger = False
        if i <= 1: continue
        for j in range(2, int(i**(0.5))+1):
            if i%j == 0:
                trigger = True
                break
        if trigger:
            continue
        elif not trigger:
            answer+=1

    return answer