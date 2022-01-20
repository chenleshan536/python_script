s=[1.34,123456.789,54321.6789,87654.45678,54321.45678]
print('排序前的身高序列')
print(s)
for i in range(0,4):
   for j in range(0,4):
      if s[j]>s[j+1]:
         s[j],s[j+1]=s[j+1],s[j]
print("排序后的身高序列：")
print(s)
