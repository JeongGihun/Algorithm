import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = 0
        stack = []
        for token in tokens :
            if token not in '+-*/' :
                stack.append(int(token))
            else :
                t2 = stack.pop()
                t1 = stack.pop()
            
                if token == '+' :
                    tmp = t1 + t2
                elif token == '-' :
                    tmp = t1 - t2
                elif token == '*' :
                    tmp = t1 * t2
                elif token == '/' :
                    tmp = int(t1 / t2)
                stack.append(tmp)
        return stack[0]
        