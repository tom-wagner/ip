class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        larger_string, smaller_string = (s1, s2) if len(s1) >= len(s2) else (s2, s1)
        larger_string_dict = {}
        for char in larger_string:
            if char in larger_string_dict:
                larger_string_dict[char] += 1
            else:
                larger_string_dict[char] = 1

        for char in smaller_string:
            char_count = larger_string_dict.get(char)
            if char_count and char_count > 0:
                larger_string_dict[char] -= 1
            else:
                return False
        return True


