def solution(genres, plays):
    music = {}
    answer = []
    for i, (g, p) in enumerate(zip(genres, plays)):
        if music.get(g) is None:
            music[g] = []
        music[g].append((p, i))

    for i in music:
        music[i].sort(key = lambda x: -x[0])
    music = sorted(list(music.values()), key = lambda x: sum(list(zip(*x))[0]))
    
    for x in reversed(music):
        for j in x[:2]:
            answer.append(j[1])
    return answer