year = int(input())

print(int((not year%400 or year%100) and not year%4))