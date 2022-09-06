def solution(arr, divisor):
    answer = sorted(list(filter(lambda x: (x/divisor).is_integer(),arr)))
    return answer if answer else [-1]

# def solution(arr, divisor):
#     return sorted(list(filter(lambda x: (x/divisor).is_integer(),arr))) or [-1]
# 조건이 없을 시 'or' 키워드 사용법 참고