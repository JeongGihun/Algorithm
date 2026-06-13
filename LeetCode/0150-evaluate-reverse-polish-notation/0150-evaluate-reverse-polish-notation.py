class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        make_num_token = []
        stack = []
        for i in tokens :
            if i in '+-*/' :
                make_num_token.append(i)
            else :
                make_num_token.append(int(i))

        for i in make_num_token :
            stack.append(i)
            while len(stack) >= 3 and isinstance(stack[-3], int) and isinstance(stack[-2], int) and isinstance(stack[-1], str) :  
                    chk =  stack.pop()
                    tmp1 = stack.pop()
                    tmp2 = stack.pop()
                    if chk == '+' :
                        stack.append(tmp2+tmp1)
                    if chk == '-' :
                        stack.append(tmp2-tmp1)
                    if chk == '/' :
                        stack.append(int(tmp2/tmp1))
                    if chk == '*' :
                        stack.append(tmp2*tmp1)
        return stack[0]