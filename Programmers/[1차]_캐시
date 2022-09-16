def solution(cacheSize, cities):
    answer = 0
    cache = []
    for i in map(lambda x: x.lower(), cities):
        if i in cache:
            cache.remove(i)
            cache.append(i)
            answer += 1

        elif i not in cache:
            cache.append(i)
            if len(cache) > cacheSize:
                cache.pop(0)

            answer += 5

    return answer