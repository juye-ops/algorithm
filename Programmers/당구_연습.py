def solution(m, n, startX, startY, balls):
    answer = []
    dist_sq = lambda x1, x2, y1, y2: (x2-x1)**2 + (y2-y1)**2
    for x, y in balls:
        tmp = []
        if startY != y:
            tmp.append(dist_sq(startX, 2*m-x, startY, y))
            tmp.append(dist_sq(startX, -x, startY, y))
        else:
            if startX > x:
                tmp.append(dist_sq(startX, 2*m-x, startY, y))
            if startX < x:
                tmp.append(dist_sq(startX, -x, startY, y))

        if startX != x:
            tmp.append(dist_sq(startX, x, startY, 2*n-y))
            tmp.append(dist_sq(startX, x, startY, -y))
        else:
            if startY > y:
                tmp.append(dist_sq(startX, x, startY, 2*n-y))
            if startY < y:
                tmp.append(dist_sq(startX, x, startY, -y))
        answer.append(min(tmp))
            
    return answer
