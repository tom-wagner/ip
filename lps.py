class Solution:
    def longestPalindrome(self, s: str) -> str:
        lcs = ''
        for i in range(0, len(s)):  # n
            for j in range(i, len(s)):  # n
                substring = s[i:j + 1]
                if substring == substring[::-1] and len(substring) > len(lcs):
                    lcs = substring
        return lcs


s = Solution()

print(s.longestPalindrome('babad'))
