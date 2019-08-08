class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) == len(t) and len(s) > 0:
            return sum([0 if char == t[idx] else 1 for idx, char in enumerate(s)]) == 1
        if abs(len(s) - len(t)) == 1:
            insert_count = 0
            longer, shorter = (s, t) if len(s) > len(t) else (t, s)
            for idx, char in enumerate(longer):
                if shorter[idx - insert_count] != longer[idx]:
                    insert_count += 1

                # short circuit
                if insert_count > 1:
                    return False
            return insert_count == 1
        return False


s = Solution()

print(s.isOneEditDistance('a', ''))
