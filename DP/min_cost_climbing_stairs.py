# https://leetcode.com/problems/min-cost-climbing-stairs/
# Approach is ki 1st two toh base cases hai then on the third step we calculate minimum of cost + index of both the previous two stairs 


# Recursive Naive approach (giving TLE)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        def DP(i):
            if i < 2:
                return 0
            return min(cost[i-2] + DP(i-2), cost[i-1] + DP(i-1))
        return DP(n)


# Bottom up approach (Tabulation)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n < 2:
            return 0
        dp = [0] * (n+1)

        for i in range(2, n+1):
            dp[i] = min(cost[i-2] + dp[i-2], cost[i-1] + dp[i-1])
        return dp[n]


# Top-down approach (Memoization)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {0: 0, 1: 0}

        def f(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = min(cost[x-2] + f(x-2), cost[x-1] + f(x-1))
                return memo[x]
        return f(len(cost))
