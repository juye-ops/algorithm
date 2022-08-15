def solution(word):
    answer = 0
    odd = "AEIOU"
    pattern = [1, 6, 31, 156, 781]
    for i in range(len(word)):
        answer+=(pattern[4-i] * odd.find(word[i]))+1
    
    # A
    # AA
    # AAA
    # AAAA
    # AAAAA
    # AAAAE
    # 5 -> 6*5 -> 31*5 -> 156*5 -> 781*5
    return answer