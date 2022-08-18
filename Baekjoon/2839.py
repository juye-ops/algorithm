a = int(input())

weight3=[0,2,4,1,3]
weight5=[2,1,0,2,1]

if a<=9:
    if a == 3: print(1)
    elif a == 5: print(1)
    elif a == 6:print(2)
    elif a == 8:print(2)
    elif a == 9:print(3)
    else: print(-1)

else:
    x, y = divmod(a, 5)
    print(weight3[y] + weight5[y]+(x-2))