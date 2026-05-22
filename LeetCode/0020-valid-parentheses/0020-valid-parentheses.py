class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        l = list(s)
        while l :
            tmp = l.pop()
            stack.append(tmp)
            while l and stack :
                if l[-1] == "(" and stack[-1] == ")" :
                    l.pop()
                    stack.pop()
                elif l[-1] == "[" and stack[-1] == "]" :
                    l.pop()
                    stack.pop()
                elif l[-1] == "{" and stack[-1] == "}" :
                    l.pop()
                    stack.pop()
                else :
                    break
        if not stack and not l :
            return True
        else :
            return False