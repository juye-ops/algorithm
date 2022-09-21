import math
from collections import defaultdict


def time_to_int(time):
    h, m = time.split(":")

    return int(h)*60 + int(m)

def solution(fees, records):
    answer = []
    parked = {}
    data = defaultdict(int)
    for i in records:
        time, car_number, status = i.split(" ")

        if status == "IN":
            parked[car_number] = time_to_int(time)

        elif status == "OUT":
            data[car_number] += (time_to_int(time) - parked[car_number])
            del parked[car_number]

    for i in parked:
        data[i] += time_to_int("23:59") - parked[i]

    d_time, d_fee, time_per, fee_per = fees
    for i in sorted(data, key = int):
        total = data[i] - d_time
        if total < 0:
            answer.append(d_fee)
            continue

        answer.append(d_fee + math.ceil(total/time_per) * fee_per)

    return answer