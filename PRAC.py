nums = [1, 2, 3, 4, 5, 9, 7]


class Solution:
    def sortedSquares(self, nums):
        arr = []
        for num in nums:
            arr.append(num * num)
        arr.sort()
        return arr
    
    def reverse(self, nums):
        l = 0
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums

solution = Solution()
print(nums)
print(solution.sortedSquares(nums))

print(solution.reverse(nums))
