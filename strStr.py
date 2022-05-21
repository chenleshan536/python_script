def strStr( haystack: str, needle: str) -> int:
    l=[]
    j=[]
    n=0
    for i in haystack:
        l.append(i)
    for k in needle:
        j.append(k)
    for m in range(len(l)):
        for o in range(len(j)):
            if l[m] == j[o]:
                n = n+1
            continue
    if n == len(j):
        








length = strStr('laksdhf', 'dh')
print(length)