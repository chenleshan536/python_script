def IsPrimeNumber(n):
    if n < 2:
        return False
    
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return False
    return True

while True:
    try:
        character = input("please input a number: ")
        a=int(character)
        
        if IsPrimeNumber(a):
            print(str(a) + " is a prime number")
        else:
            print(str(a) + " is not a prime number")
    except :
        print("invalid input number", character)
