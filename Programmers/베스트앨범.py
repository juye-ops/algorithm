from collections import defaultdict

def solution(genres, plays):
    a = defaultdict(lambda: [])
    for i, x in enumerate(zip(genres, plays)):
        a[x[0]].append((i, x[1]))
    a = sorted(a.values(), key = lambda x: sum(map(lambda y: y[1], x)), reverse=True)
    a = list(map(lambda x: sorted(x, key = sum, reverse=True)[:2], a))
    a = [x if len(x) != 2 or x[0][1] != x[1][1] else [x[1], x[0]] for x in a]
    return [x[0] for x in sum(a, [])]