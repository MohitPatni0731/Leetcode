# https://leetcode.com/problems/climbing-stairs/
# Thinking - there is pattern going on after two base cases which is simply the sum of last two function output 

## Recursive naive approach
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        return self.climbStairs(n-1) + self.climbStairs(n-2)
