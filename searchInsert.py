def searchInsert( nums: list[int], target: int) -> int:
    for i in range (len(nums)):
        if nums[i]==target:
                return i
    if target<nums[0]:
        return 0
    for i in range (len(nums)):
        if nums[i]+1==target:
            return i+1
        if nums[i]-1==target:
            return i
    if target>nums[len(nums)-1]:
        return len(nums)

earchInsert2 = searchInsert([3,6,7,8,10],5)
print(earchInsert2)