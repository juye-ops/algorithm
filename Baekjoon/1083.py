def solution(N, nums, S):
    while S:
        for i in range(N):
            _max = i
            for j in range(i, i+S+1):
                if j >= N:
                    break
                
                if nums[j] > nums[_max]:
                    _max = j
            
            if _max != i:
                S -= (_max-i)
                nums.insert(i, nums.pop(_max))
                break
        else:
            break
    
    print(*nums, sep=" ")


N = int(input())
nums = list(map(int, input().split()))
S = int(input())

solution(N, nums, S)

# 1 2 5 4 3 6 7 8 9
# 5

## i ~ S칸까지 arr[i]보다 큰게 있나?