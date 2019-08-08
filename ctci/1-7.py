from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left, right, top, bot = 0, len(matrix) - 1, 0, len(matrix) - 1
        m_len = len(matrix) - 1
        for i in range(0, len(matrix) // 2):
            for j in range(left, right):
                # NOTE: right - j and bot - j is leading to a bug on inner rotations
                matrix[j][right], matrix[bot][m_len - j], matrix[m_len - j][left], matrix[top][j] = matrix[top][j], matrix[j][right], matrix[bot][m_len - j], matrix[m_len - j][left]
            top, left = top + 1, left + 1
            right, bot = right - 1, bot - 1
        return matrix


s = Solution()

print(s.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))

# for i in range(0, 4 // 2):
#     print(i)
