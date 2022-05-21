cakename=['冰雪奇缘','悉尼之风']
cakeprice=[120,100]
flag=str(0)
while flag==str(0):
    print('请输入蛋糕信息：')
    addname=input('蛋糕名：')
    addprice=input('价格：')
    if addname in cakename:
        print('添加失败，该蛋糕信息已存在\n')
    else:
        cakename.append(addname)
        cakeprice.append(addprice)
        print('添加成功！\n')
    flag=input('继续添加？1退出，0继续…………………………………………………………………………')
    if flag==1:
        break
print(cakename,cakeprice)
