# https://leetcode.com/problems/partition-equal-subset-sum/description/
# Appraoch agar array diya hai aur usme 2 subset hai toh ek subset ka sum toh whole array ke sum divide 2 ke barabar hoga na 

# toh isko just even odd ke perspective se kiya toh 124/144 test case paas ho gaye LC pe 
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 0:
            return True
        else:
            return False

# DP Appraoch - 
