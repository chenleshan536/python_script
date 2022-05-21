from unittest import skip


class Solution(object):
    def romanToInt(self, s):
        
        """
        :type s: str
        :rtype: int
        """
        shuzu = []
        zidian={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        for x in s:
            shuzu.append(zidian[x])


        #print(shuzu)
        length = len(shuzu)
        a = 0
        for i in range(length-1):
            if shuzu[i]==1:
                if shuzu[i+1]==5 or shuzu[i+1]==10:
                    a = a +shuzu[i]  
            if shuzu[i]==10:
                if shuzu[i+1]==50 or shuzu[i+1]==100:
                    a = a +shuzu[i] 
            if shuzu[i]==100:
                if shuzu[i+1]==500 or shuzu[i+1]==1000:
                    a = a +shuzu[i]
        #print(a)  



        f = 0
        for j in range(length):
            f = f + int(shuzu[j])
        f = f - a - a
        #print(int(shuzu[j]))
        return f
       

calculator = Solution()
int_value = calculator.romanToInt("MCMXCIV")
print("MCMXCIV is ", int_value)




