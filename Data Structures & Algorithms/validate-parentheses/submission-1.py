class Solution:
    def isValid(self, s: str) -> bool:
        
        opening = ['[', '(', '{']

        stack = []

        for c in s:
            if c in opening:
                stack.append(c)

            else:
                if not stack:
                    return False

                top = stack.pop()

                if ((top == '(' and c != ')')
                    or top == '[' and c != ']'
                    or top == '{' and c != '}'):
                    return False

        
        return not stack