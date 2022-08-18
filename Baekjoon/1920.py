import sys

sys.setrecursionlimit(10 ** 9)


def search(lst, n, left, right):
    if left > right: return 0
    mid = (left + right) // 2
    mid_val = lst[mid]

    if n == mid_val:
        return 1
    elif n < mid_val:
        return search(lst, n, left, mid - 1)
    elif n > mid_val:
        return search(lst, n, mid + 1, right)


input()

lst = sorted(list(map(int, input().split())))

input()

for i in list(map(int, input().split())):
    print(search(lst, i, 0, len(lst)-1))
