# https://leetcode.com/problems/unique-paths/description/
# Aprroach - jo base case hai waha pe toh start hoga means 1 step to reach 0,0 then bahut saari conditions laga ke ye check karenge ki i ya j 

# Recursive naive approach
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def paths(i, j):
            if i == j == 0:
                return 1
            elif i < 0 or j < 0 or i == m or j == n:
                return 0
            else:
                return paths(i, j-1) + paths(i-1, j)
        
        return paths(m-1,n-1)
