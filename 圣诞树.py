def tree(t):
    for i in range(1,t+1):
        print(" "*(t-i),end="")
        print("*"*(2*i-1))
n =int(input("请输入圣诞树树冠行数>>>"))
tree(n)
print(" "*(n-2),"*")
print(" "*(n-2),"*")
print(" "*(n-2),"*")
