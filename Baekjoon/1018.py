def slicing(chess, x, y):
    return [i[x:x+8] for i in chess[y:y+8]]
        
    

M, N = map(int, input().split())

chess = [input() for _ in range(M)]
answer = None

for y in range(M-7):
    for x in range(N-7):
        chess88 = slicing(chess, x, y)  # 8*8 짜리로 일단 슬라이싱
        answer1 = 0
        answer2 = 0
        
        # 8*8 순회
        ## 시작이 B일 때
        for a in range(8):
            for b in range(8):
                if (a+b)%2 == 0:
                    if chess88[a][b] == "W":
                        answer1 += 1
                
                if (a+b)%2 == 1:
                    if chess88[a][b] == "B":
                        answer1 += 1
        
        ## 시작이 W일 때
        for a in range(8):
            for b in range(8):
                if (a+b)%2 == 0:
                    if chess88[a][b] == "B":
                        answer2 += 1
                
                if (a+b)%2 == 1:
                    if chess88[a][b] == "W":
                        answer2 += 1
        if answer is None:
            answer = min(answer1, answer2)
        else:
            answer = min(answer1, answer2, answer)
                    
                    
                    
print(answer)