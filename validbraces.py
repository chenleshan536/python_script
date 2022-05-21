from unittest import skip
class Solution(object):
    def isValid(self, s):
        xiao = 0
        zhong = 0
        da = 0
        last_brace_type = -1 # () 0, [] 1, {} 2, invalid -1
        for i in s:
            if s=='(':
                xiao = xiao +1
                last_brace_type = 0
            elif s==')':
                if last_brace_type ==0:
                    xiao = xiao -1
                    #change back to original last_brace_type
                else:
                    return False
            elif s=='[':
                zhong = zhong +1
                last_brace_type = 1
            elif s==']':
                zhong = zhong-1
            elif s=='{':
                da = da +1
            elif s=='}':
                da = da -1
        
        print(xiao, zhong, da)
        return xiao==0 and zhong==0 and da==0
            
calculator = Solution()
prefix = calculator.isValid("([)]")
print(prefix)         