def find_length(nums, k):
    left = ans = curr = 0

    for right in range(len(nums)):
        curr += nums[right]
        while curr > k:
            curr -= nums[left]
            left += 1
        
        ans = max(ans, right - left + 1)
    return ans

nums = [1,2,3,4,5,6,7,8,9,10]

k = 10

print(find_length(nums, k))