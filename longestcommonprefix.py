from unittest import skip


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """    
        
        prefix = str(strs[0])
        while True:
            shifouzhaodao = True
            for a in range(1,len(strs),1):
                current = str(strs[a])
                #print("current, " current)
                #print("prefix", prefix)
                if current.startswith(prefix)==False: 
                    z=prefix[len(prefix)-1]
                    
                    prefix=prefix.removesuffix(z)
                    shifouzhaodao = False
            if shifouzhaodao==True:
                break
        return prefix
                


calculator = Solution()
prefix = calculator.longestCommonPrefix(["flower","flow","flight"])
print(prefix)