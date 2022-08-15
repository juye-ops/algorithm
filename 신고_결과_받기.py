def solution(id_list, report, k):
    answer = []
    ids={x:[] for x in id_list}
    cnt = {x: 0 for x in id_list}
    report = list(set(report))
    for i in report:
        a, b = i.split(" ") #a reported b
        ids[b].append(a)
    for i in ids:
        if len(ids[i]) >= k:
            for j in ids[i]:
                cnt[j] += 1
    return list(cnt.values())