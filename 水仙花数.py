a=1
b=0
c=0
while a*100+b*10+c<1000:
    if (a*a*a+b*b*b+c*c*c)==(a*100+b*10+c):
        print(str(a),str(b),str(c))
    elif c>9:
        c=0
        b=b+1
    elif b>9:
        b=0
        a=a+1
    
    
    
