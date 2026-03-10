class Solution:
    def Twosun(self, nums:List[int], target: int):
        h ={}
        for i , num in enumerate(nums):
            h[num] = i
        
        for i, num in enumerate(nums):
            desired = target - num
            if desired in h and h[desired] !=i:
                return i, h[desired]
# 1. Create the instance of the class
solver = Solution()

# 2. Define your test data
my_nums = 
my_target = 9

# 3. Call the method and store the result
result = solver.Twosun(my_nums, my_target)

# 4. Print the result
print(f"Indices found: {result}")