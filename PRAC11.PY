class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in dic: # This operation is O(1)!
                return [i, dic[complement]]
            
            dic[num] = i
        
        return [-1, -1]
    
nums = [2, 11, 7, 15]
target = 9
solution = Solution()
result = solution.twoSum(nums, target)
print(result) # Output: [1, 0]
