a, b = map(int, input().split())

print(" ".join(map(str, filter(lambda x: x < b, map(int, input().split())))))