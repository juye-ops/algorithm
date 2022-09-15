def solution(n, words):
    users = {x: [] for x in range(1, n+1)}
    for i, word in enumerate(words):
        user = i%n + 1
        users[user].append(word)
        if word in words[:i] or (i >= 1 and words[i-1][-1] != word[0]):
            return [user, len(users[user])]

    return [0, 0]