def findMaxAverage(nums, k):
    curr = 0
    for i in range(k):
        curr += nums[i]
    
    ans = curr
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i-k]
        ans = max(ans, curr)
    return ans/k

nums = [1,12,-5,-6,50,3]
k = 4

print(findMaxAverage(nums, k))