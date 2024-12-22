# https://leetcode.com/problems/climbing-stairs/
# Thinking - there is pattern going on after two base cases which is simply the sum of last two function output (see the image in DP folder for approach)

## Recursive naive approach
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        return self.climbStairs(n-1) + self.climbStairs(n-2)


## Top-down approach (Memoization)
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1: 1, 2: 2}

        def f(x):
            if x in memo:
                return memo
            else:
                memo[x] = f(x-1) + f(x-2)
                return memo[x]
        return f(n)


## Bottom-Up approach (Tabulation)
class Solution:
    def climbStairs(self, n: int) -> int:
        DP = [0] * (n+1)
        DP[0] = 1
        DP[1] = 2
        for i in range(2, n+1): 
            DP[i] = DP[i-1] + DP[i-2]
        return DP[-2]
