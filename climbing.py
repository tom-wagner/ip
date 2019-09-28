class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1: 1, 2: 2}
        current_stair = 3
        while True:
            if current_stair > n:
                return memo[n]
            memo[current_stair] = memo[current_stair - 1] + memo[current_stair - 2]
            current_stair += 1


s = Solution()

print(s.climbStairs(5))