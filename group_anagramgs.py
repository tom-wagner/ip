from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str in seen:
                seen[sorted_str].append(s)
            else:
                seen[sorted_str] = [s]

        return list(seen.values())
