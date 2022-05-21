def plusOne(digits: list[int]) -> list[int]:
    digits[len(digits)-1]=digits[len(digits)-1]+1
    for a in range(len(digits)-1,-1,-1):
        if digits[a]==10:
            digits[a-1]=digits[a-1]+1
            digits[a]=0
    if digits[0]==0:
        digits.insert(0,1)
        




    return digits






A = plusOne([4,3,2,1])