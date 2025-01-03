# https://leetcode.com/problems/maximum-product-subarray/description/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == 0:
                curr_max = 0
                curr_min = 0
                res = max(res, 0)
                continue

            temp_max = max(curr_max * nums[i], curr_min * nums[i], nums[i])
            temp_min = min(curr_max * nums[i], curr_min * nums[i], nums[i])

            curr_max = temp_max
            curr_min = temp_min 

            res = max(res, temp_max)
        return res
