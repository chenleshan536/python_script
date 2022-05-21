def fibonachi(n:int)->int:
    if n == 1 or n == 2:
        return 1
    else:
        return fibonachi(n-1)+fibonachi(n-2)


def fibonachi2(n:int)->int:
    if n == 1 or n == 2:
        return 1

    result = [0 for i in range(n)]
    result[0] = 1
    result[1] = 1

    for i in range(2, n):
        result[i] = result[i-1] + result[i-2]
    
    return result[n-1]


print(fibonachi2(200000))

steps=int(input())
step=steps//2
odd=1
even=1
for i in range(1,step+1):
    odd=odd+even
    even=odd+even
if steps%2==0:
    print(odd)
elif steps%2==1:
    print(even)