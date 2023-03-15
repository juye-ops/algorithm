def solution(N, M, dictionary, target):
    iton = dict(dictionary)
    rev_dictionary = map(lambda x: (x[1], x[0]), dictionary)
    ntoi = dict(rev_dictionary)
    for i in target:
        if i.isdigit():
            print(iton[int(i)])
        else:
            print(ntoi[i])

N, M = map(int, input().split())
dictionary = [(i, input()) for i in range(1, N+1)]
target = [input() for _ in range(M)]
solution(N, M, dictionary, target)