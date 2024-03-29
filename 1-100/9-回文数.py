# -*- encoding: utf-8 -*-
"""
@File    :   9-回文数.py
@Time    :   2023/06/09 20:11:02
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
"""
"""
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
"""
x = int(input("请输入一个数:"))
if x < 0:
    print(False)
else:
    y = str(x)[::-1]
    if y == str(x):
        print(True)
    else:
        print(False)
# 特别慢，思路简单
x = int(input("请输入一个数:"))
if x < 0:
    print(False)
else:
    x = str(x)
    ll, r = 0, len(x) - 1
    while ll < r:
        if x[ll] != x[r]:
            print(False)
        ll += 1
        r -= 1
    print(True)
# 时间稍微短点 判断字符串左边递加是否等于右边递减
