def where(n):
    return ((n - 1) % 3, (n - 1) // 3) if n != 0 else (1, 3)


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def solution(numbers, hand):
    answer = ""
    l = r = (0, 3)
    for i in numbers:
        i_where = where(i)

        if i in [1, 4, 7]:
            answer += "L"
            l = i_where

        elif i in [3, 6, 9]:
            answer += "R"
            r = i_where

        else:
            l_dis = distance(l, i_where)
            r_dis = distance(r, i_where)

            if l_dis == r_dis:
                answer += hand[0].upper()
                if hand == "right":
                    r = i_where
                elif hand == "left":
                    l = i_where

            elif l_dis < r_dis:
                answer += "L"
                l = i_where
            elif r_dis < l_dis:
                answer += "R"
                r = i_where

    return answer