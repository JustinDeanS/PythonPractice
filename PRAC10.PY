
def waysToSplitArray(nums):
    n = len(nums)

    prefix = nums[0]

    for i in range(1, len(nums)):
        prefix.append(nums[i]+ prefix[-1])
    
    ans = 0

    for i in range(len(nums)-1):
        l = prefix[i]
        r = prefix[-1] - prefix[i]
        if l >= r:
            ans += 1
    return ans

nums = [1,2,3,4]



for i in range(0, 2):
    print('1')

