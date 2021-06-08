'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
'''
x=int(input('请输入一个数:'))
if x <0:
    print( False)
else:
    y=str(x)[::-1]
    if y==str(x):
        print(True)
    else :
        print(False)
#特别慢，思路简单
x=int(input('请输入一个数:'))
if x <0:
    print( False)
else:
    x=str(x)
    l, r = 0, len(x) - 1
    while l < r:
        if x[l] != x[r]:
            print(False)
        l += 1
        r -= 1
    print(True)
#时间稍微短点 判断字符串左边递加是否等于右边递减

