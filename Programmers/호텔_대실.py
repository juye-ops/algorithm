def to_minute(time):
    h, m = time.split(":")
    minute = int(h) * 60 + int(m)
    return minute

def solution(book_time):
    answer = 0
    
    book_time = sorted(book_time, key=lambda x: to_minute(x[0]))
    rooms = {}
    for i in book_time:
        s = to_minute(i[0])
        e = to_minute(i[1])
        for room in rooms:
            if rooms[room] <= s:
                rooms[room] = e+10
                break
        else:
            answer+=1
            rooms[answer] = e+10
    return answer