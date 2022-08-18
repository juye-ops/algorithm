import json

def solution(s):
    t = []
    s = s.replace("{", "[").replace("}", "]")
    slist = json.loads(s)

    slist = sorted(slist, key=len)
    for i in slist:
        for j in i:
            if j not in t:
                t.append(j)
    return t