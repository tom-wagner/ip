from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest_idx = 0
        for i, max_jump in enumerate(nums):
            if i > furthest_idx:
                return False
            if furthest_idx >= len(nums) - 1:
                return True
            furthest_idx = max(furthest_idx, i + max_jump)
        return True

