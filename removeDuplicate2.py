class Solution:
    def removeDuplicates(self, nums) -> int:
        nums2=[]
        for a in nums:
            if a not in nums2:
                nums2.append(a)
            else:
                pass
        return len(nums2),nums2






calculator = Solution()
new_array = calculator.removeDuplicates([1,1,2,2,3,3,4,4,5,5,6,6])
print(new_array)

