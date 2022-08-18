A = int(input())
B = input()
answer = 0
for i in range(len(B)-1, -1, -1):
    t = int(A) * int(B[i])
    print(t)
    answer += t*(10**(len(B)-i - 1))
print(answer)