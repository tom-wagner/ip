forward_chars = {'(', '{', '['}
validity_map = {'(': ')', '{': '}', '[':']'}

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        for char in s:
            if char in forward_chars:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False

                top_of_stack = stack.pop()
                if validity_map[top_of_stack] == char:
                    continue
                else:
                    return False

        return len(stack) == 0
