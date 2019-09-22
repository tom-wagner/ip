from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def recurse(nums: List[int], curr: List[int] = [], curr_sum: int = 0, tgt: int = target):
            nonlocal combinations
            if curr_sum == tgt:
                combinations.append(curr)
                return
            if curr_sum > tgt:
                return

            for i in range(0, len(nums)):
                curr_num = nums[i]
                recurse(nums=nums[i:], curr=curr + [curr_num], curr_sum=curr_sum + curr_num)

        recurse(nums=candidates)
        return combinations


s = Solution()

print(s.combinationSum([2, 3, 5], 8))
