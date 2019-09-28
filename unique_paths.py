class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[1] * m for _ in range(0, n)]
        for r in range(1, n):
            for c in range(1, m):
                matrix[r][c] = matrix[r - 1][c] + matrix[r][c - 1]
        return matrix[n - 1][m - 1]


s = Solution()

print(s.uniquePaths(7, 3))
