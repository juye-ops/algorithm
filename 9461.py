from collections import deque

for i in range(int(input())):
    a = int(input())
    pattern = deque([1, 1, 1, 2, 2])
    if a < 5:
        pattern.rotate(5-a)
    for i in range(a-5):
        pattern.append(pattern.popleft() + pattern[-1])
    print(pattern.pop())
