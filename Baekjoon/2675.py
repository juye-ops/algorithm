T = int(input())
cnt_str = [input() for _ in range(T)]

for x in cnt_str:
    cnt, string = x.split()
    answer = ""
    for i in string:
        answer += i*int(cnt)
    print(answer)