def solution(record):
    answer = []
    DB = dict()
    for i in record:
        CMD = i.split()
        if not DB.get(CMD[1]):
                DB[CMD[1]] = CMD[2]
        if CMD[0] in ["Enter", "Change"]:
            DB[CMD[1]] = CMD[2]
    for i in record:
        CMD = i.split()
        if CMD[0] == "Enter":
            answer.append(f"{DB[CMD[1]]}님이 들어왔습니다.")
        elif CMD[0] == "Leave":
            answer.append(f"{DB[CMD[1]]}님이 나갔습니다.")

    return answer