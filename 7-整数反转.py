'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
'''

num=int(input('请输入一个数:'))
if num >=0:
    num = str(num)
    a=[]
    num=''.join(num)
    count=len(num)
    for i in range(len(num),0,-1):
        count-=1
        a.append(num[count])
    b=''.join(a)
    print(int(b))
else:
    num=str(num)
    b=[]
    a=num[1:]
    print(a)
    count=len(a)
    for i in range(len(a),0,-1):
        count-=1
        b.append(a[count])
    c=''.join(b)
    print(num[0]+c)

x=int(input('请输入一个数:'))
if x>0:
    x=str(x)
    new=''
    for i in range(len(x)-1,-1,-1):
        new=new+x[i]
    new=int(new)
    if new>=2**31-1:
        new=0
    print(new)
else:
    x=str(-x)
    new = ''
    for i in range(len(x) - 1, -1, -1):
        new = new + x[i]
    new=int(new)
    new=-new
    if new<=-2**31:
        new=0
    print(new)






