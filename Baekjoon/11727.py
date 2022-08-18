lst = [1, 3]
a = int(input())
for i in range(2, a):
    lst.append(2*lst[i-2]+lst[i-1])

print(lst[a-1]%10007)