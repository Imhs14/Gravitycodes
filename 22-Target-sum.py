class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {nums[0] : 0}
        for i in range(1, len(nums)):
            a = target - nums[i]
            if a in seen.keys() and i != seen[a]:
                return [seen[a], i]
            
            seen[nums[i]] = i