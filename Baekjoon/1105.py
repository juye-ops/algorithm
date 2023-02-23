L, R = input().split()

answer = 0

if len(L) == len(R):
    for l, r in zip(L, R):  # 앞에서부터 같으면 pass, 8이면 answer+=1 
        if l == r:
            if l == r == "8":  
                answer += 1
        else:
            break
print(answer)