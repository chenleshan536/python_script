def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """

    if n != 0:
        for i in range(0,n):
            nums1[m+i] = nums2[i]
    for i in range(0,len(nums1)-1):
        for j in range(0,len(nums1)-1):
            if nums1[j]>nums1[j+1]:
                a=nums1[j]
                nums1[j]=nums1[j+1]
                nums1[j+1]=a

        



nums1=[1,2,3,0,0,0]
merge(nums1,3,[2,5,6],3)
print(nums1)