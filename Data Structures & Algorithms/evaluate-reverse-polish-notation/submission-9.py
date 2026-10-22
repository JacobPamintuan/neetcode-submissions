class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for tok in tokens:
            if tok not in ["+", "-", "*", "/"]:
                stack.append(int(tok))
            else:
                b = stack[-1]
                stack.pop()
                a = stack[-1]
                stack.pop()

                if tok == "+":
                    stack.append(a+b)
                elif tok == "-":
                    stack.append(a-b)
                elif tok == "*":
                    stack.append(a*b)
                elif tok == "/":
                    stack.append(int(a/b))


        return stack[0]

