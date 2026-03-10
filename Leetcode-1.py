class Solution(object):
    
    def twoSum(self, nums, target):
        self.nums = nums
        self.target = target
    def inputs(self):
        self.nums = [int(x) for x in (input().split())]
        self.target = int(input())
    def logic(self):
        n = len(self.nums)
        for i in range(n):
            for j in range(i+1,n):
                if self.nums[i] + self.nums[j] == self.target:
                    return [i,j]

solver = Solution()

solver.inputs()
result = solver.logic()
print(f"{result}")