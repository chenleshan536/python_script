a=input("a:")
jj=input("+/-?>>>")
b=input("b:")
c=input("c:")
if jj=="+":
    c=float(c)-float(b)
else :
    c=float(c)+float(b)
c=c/float(a)
print("x="+str(c))
