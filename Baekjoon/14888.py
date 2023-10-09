import sys
input = sys.stdin.readline

maxval = int(-1e9)
minval = int(1e9)

def dfs(nums, opers, val):
    global maxval, minval
    if not nums:
        maxval = max(maxval, val)
        minval = min(minval, val)
        return
    
    if opers[0]:
        new_opers = [opers[0]-1, opers[1], opers[2], opers[3]]
        dfs(nums[1:], new_opers, val+nums[0])
    
    if opers[1]:
        new_opers = [opers[0], opers[1]-1, opers[2], opers[3]]
        dfs(nums[1:], new_opers, val-nums[0])
    
    if opers[2]:
        new_opers = [opers[0], opers[1], opers[2]-1, opers[3]]
        dfs(nums[1:], new_opers, val*nums[0])

    if opers[3]:
        new_opers = [opers[0], opers[1], opers[2], opers[3]-1]
        dfs(nums[1:], new_opers, int(val/nums[0]))

N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))

dfs(nums[1:], operators, nums[0])
print(maxval, minval, sep="\n")