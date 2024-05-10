class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening_brackets = {"(", "{", "["}
        bracket_map = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in opening_brackets:
                stack.append(char)
            elif char in bracket_map:
                if not stack or stack.pop() != bracket_map[char]:
                    return False
            else:
                # Ignore characters other than brackets
                continue

        return not stack
