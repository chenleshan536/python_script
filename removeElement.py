def removeElement(nums: list[int], val: int) -> int:
    l=[]
    for i in range(len(nums)):
        if nums[i]==val:
            l.append(i)
    for j in range (len(l)-1,-1,-1):
        nums.pop(l[j])
    return len(nums)


        


array = [0,1,2,2,3,0,4,2]
length = removeElement(array, 2)
print(length)
print(array)