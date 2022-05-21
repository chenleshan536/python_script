from unittest import skip
class Solution(object):
    def isValid(self, s):
        a = ['j']
        for char in s:
            

            if a[-1] =='(':
                if char==')':
                    a.pop()
                    continue
            if a[-1] =='[':
                if char==']':
                    a.pop()
                    continue
            if a[-1] =='{':
                if char=='}':
                    a.pop()
                    continue
            a.append(char)

        return len(a)==1
            
calculator = Solution()
prefix = calculator.isValid("[]{})")
print(prefix)         