import itertools

def solution(numbers):
    ans = []
    for i in range(1, len(numbers)+1):
        permute = list(itertools.permutations(list(numbers), i))
        for j in permute:
            trg = False
            val = int("".join(j))
            for k in range(2, int(val**0.5) + 1):
                if val%k==0:
                    trg = True
                    break
            if not trg:
                ans.append(val)
    answer = set(ans)
    if 0 in answer:
        answer.remove(0)
    if 1 in answer:
        answer.remove(1)
    print(answer)

    return len(answer)