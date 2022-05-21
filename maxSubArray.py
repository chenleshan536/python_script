def maxSubArray( nums: list[int]) -> int:

    maximum = 0
    sum = 0
    
    for i in range(len(nums)):
        sum = sum + nums[i]
        if sum <= 0:
            # drop everything till now and reset
            sum = 0
        else:
            if sum > maximum:
                maximum = sum

    return maximum




    # for a in range (len(nums)):
    #     if nums[a]>0:
    #         b = b+nums[a]
    #     elif nums[a]<0:
    #         d=d+nums[a]
    #         for c in range (a+1,len(nums)):
    #             if nums[c]<0:
    #                 d= d+nums[c]
    #             elif nums[c]>0:
    #                 for e in range (c+1,len(nums)):
    #                     h=e
    #                     if nums[e]>0:
    #                         f = f + nums[e]
    #                     else:
    #                         break
    #         if f>d:
    #             for g in range(a+1,h-1):
    #                 b = b+nums[g]
    #         elif d>f:
    #             continue

def trimNegativeValues(nums: list[int]) -> list[int]:
    return nums
                        




maxSummary = maxSubArray([3,6,7-90,8,10])
print(maxSummary)