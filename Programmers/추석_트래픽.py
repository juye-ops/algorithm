def splitter(l):
    tmp = l.split()
    time = tmp[1]
    width = tmp[2]

    time = time.split(":")
    time = list(map(float, time))
    time = time[0] * 3600 + time[1] * 60 +time[2]

    width = width.rstrip("s")

    return float(time), float(width)


def solution(lines):
    t_series = list(map(splitter, lines))
    t_series = sorted(t_series, key=lambda x: float(x[0]))
    answer = 0
    for i in range(len(lines)):
        cnt = 1
        now = t_series[i][0] - 0.001
        for j in range(i+1, len(lines)):
            if (t_series[j][0] - t_series[j][1]) < now <= t_series[j][0] or (t_series[j][0] - t_series[j][1]) < now+1 <= t_series[j][0] or now < t_series[j][0]- t_series[j][1] < t_series[j][0] <= now+1:
                cnt+=1

        answer = max(cnt, answer)



    return answer
