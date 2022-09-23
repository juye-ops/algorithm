for i in range(int(input())):
    print(sum(map(lambda x: sum(range(1, len(x)+1)),input().split("X"))))