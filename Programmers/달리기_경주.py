def solution(players, callings):
    p_r = {y: x for x, y in enumerate(players)}
    r_p = {x: y for x, y in enumerate(players)}
    for i in callings:
        p_r[i] -= 1
        tmp_p = r_p[p_r[i]]
        tmp_r = p_r[i]
        p_r[tmp_p] += 1
        r_p[tmp_r+1] = tmp_p
        r_p[tmp_r] = i

    return list(r_p.values())