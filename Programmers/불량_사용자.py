from itertools import permutations

def check(users, banned_id):
    for j, k in zip(users, banned_id):
        if len(j) != len(k):
            return 0
        for m, n in zip(j, k):
            if m != n and n != "*": return 0
    return 1


def solution(user_id, banned_id):
    user_permutation = list(permutations(user_id,len(banned_id)))
    banned_Set = []

    for users in user_permutation:
        # 하나의 튜플과 비교 시작
        if check(users, banned_id):
            users = set(users)
            if users not in banned_Set:
                banned_Set.append(users)

    return len(banned_Set)