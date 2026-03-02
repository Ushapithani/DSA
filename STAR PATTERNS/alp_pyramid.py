'''
1 2 3 4 5
5 1 2 3 4 
4 5 1 2 3 
3 4 5 1 2 
2 3 4 5 1 
'''
nums = list(map(int, input("Enter numbers separated by space: ").split()))
n = len(nums)

for k in range(n):
    rotated = nums[-k:] + nums[:-k]   
    print(*rotated)