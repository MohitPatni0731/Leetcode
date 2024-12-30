# https://leetcode.com/problems/house-robber-ii/
# Aprroach - houses circle main hai matlab 1st houuse and last house main ek saath rob ni kar sakte kyoki wo adjacent hai toh isliye toh do baar dp lagao ek baar on all the array except first and ek baar all the array except last and then return kar do max of both the cases

# Bottom up (Tabulation)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        def f(nums):
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                dp[i] = max(nums[i] + dp[i-2], dp[i-1])
            return dp[-1]

        case1 = rob_linear(nums[:-1])
        case2 = rob_linear(nums[1:])

        return max(case1, case2)
