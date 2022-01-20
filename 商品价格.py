m=99
i=0
n=input("请输入价格：")
while i<6:
    if int(n)==m:
        print("猜对了！")
        i=i+6
    else:
        if int(n)>m:
            print("高了")
            n=input("请输入价格：")
        else:
            print("低了")
            n=input("请输入价格：")
        i=i+1
print("次数到了，价格是"+str(m))

    
