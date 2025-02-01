# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        solution = []

        def backtrack(i):
            if i == n:
                # jaise last main base case pahuch gaya matlab subset mil gaya toh solution ko result main copy kar denge [:] se
                result.append(solution[:])
                return 
            
            # ab do case banege ek pick karna hai aur dusra pick nahi karna hai 
            # first case - don't pick
            backtrack(i+1) # skip kar denge

            # second case - pick karenge
            solution.append(nums[i])
            backtrack(i+1)
            solution.pop()

        backtrack(0)

        return result 

# Time - O(2^n) - Kyoki har step pe 2 decision hai aur n levels hai total
