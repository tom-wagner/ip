from typing import List

# brute force
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub_array_sum = nums[0]
        for i in range(len(nums)):
            subarray_sum = 0
            for j in range(i, len(nums)):
                subarray_sum += nums[j]
                max_sub_array_sum = max(subarray_sum, max_sub_array_sum)

        return max_sub_array_sum
