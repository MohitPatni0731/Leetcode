# https://leetcode.com/problems/house-robber/
# Bahut time tak sochne ke baad bhi nahi aa rahi thi approach toh approach dekhi thi 
# Aprroach - max nikaal lo jo n-2 pe hai wo + jo current iteration pe hai , jo total_cost kya thi n-1 pe 

# Recursive naive approach
class Solution:
    def rob(self, nums: List[int]) -> int:
        def f(x):
            if x == 0:
                return nums[0]
            if x == 1:
                return max(nums[0], nums[1])
            
            return max(nums[x]+f(x-2), f(x-1))
        return f(len(nums)-1)


# Top down (Memoization)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:  
            return 0
        if n == 1:  
            return nums[0]
        
        memo = {0: nums[0], 1: max(nums[0], nums[1])}
        def f(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = max(nums[x]+f(x-2), f(x-1))
                return memo[x]
        return f(n-1)
        


# Bottom up (Tabulation)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        return dp[(len(nums))-1]
