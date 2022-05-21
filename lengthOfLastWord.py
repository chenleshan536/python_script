def lengthOfLastWord(s: str) -> int:
    z = ""
    for a in range(len(s)-1,-1,-1):
        if s[a]!=" ":
            z=s[a]+z
        elif s[a]==' ':
            break
    return z

    




A = lengthOfLastWord("welcome to this world, xiao hai")
print(A)