def solution(numbers):
    answer = []
    for i in numbers:
        binary = list(map(int, bin(i).replace("0b", "0")))
        
        for j in range(len(binary)-1, -1, -1):
            if binary[j] == 0:
                binary[j] = 1
                break
        
        if j+1 < len(binary):
            for k in range(j+1, len(binary)):
                if binary[k] == 1:
                    binary[k] = 0
                    break
                
        answer.append(int("0b"+"".join(map(str, binary)), 2))
        
            
    return answer