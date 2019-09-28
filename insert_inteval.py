from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        res = []
        new_mtg_st, new_mtg_end = newInterval
        insertion_point_found = False

        for st, end in intervals:
            if new_mtg_st <= end and new_mtg_end >= st and not insertion_point_found:
                insertion_point_found = True
                res.append([min(st, new_mtg_st), max(end, new_mtg_end)])
                continue

            if new_mtg_end <= st and not insertion_point_found:
                res.append([new_mtg_st, new_mtg_end])
                insertion_point_found = True

            last_mtg_start, last_mtg_end = res[len(res) - 1] if res else (None, None)
            if last_mtg_end and st <= last_mtg_end and insertion_point_found:
                res[len(res) - 1][1] = max(last_mtg_end, end)
                continue

            res.append([st, end])

        if not insertion_point_found:
            if new_mtg_end <= intervals[0][0]:
                return [newInterval] + intervals
            return intervals + [newInterval]
        return res


s = Solution()

print(s.insert([[1, 5]], [6, 8]))
