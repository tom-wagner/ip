from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        sorted_intervals = sorted(intervals, key=lambda mtg: mtg[0])

        first_mtg = sorted_intervals[0]
        res = [first_mtg]
        for st, end in sorted_intervals[1:]:
            last_idx = len(res) - 1
            current_end = res[last_idx][1]
            if st <= current_end:
                res[last_idx][1] = max(end, current_end)
            else:
                res.append([st, end])

        return res


s = Solution()

print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(s.merge([[1,4],[4,5]]))

