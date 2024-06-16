def check_for_target(nums, target):
    l = 0
    r = len(nums) - 1

    while l < r:
        curr = nums[l] + nums[r]
        if curr == target:
            return True
        if curr > target:
            r -= 1
        if curr < target:
            l += 1
    return False

nums = [1,2,3,4,5,6,98]

target = 99

print(check_for_target(nums, target))