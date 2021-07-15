# -*- encoding: utf-8 -*-
'''
@File    :   476-数字的补数.py
@Time    :   2021/07/15 23:32:33
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
'''
给你一个 正 整数 num ，输出它的补数。补数是对该数的二进制表示取反

示例 1：

输入：num = 5
输出：2
解释：5 的二进制表示为 101（没有前导零位），其补数为 010。所以你需要输出 2 。
示例 2：

输入：num = 1
输出：0
解释：1 的二进制表示为 1（没有前导零位），其补数为 0。所以你需要输出 0 。

既然没有限制，那就果断数学计算……
num和补数相加，就是满数位1的二进制数，即2**(n-1)-1
'''


class Solution:
    def findComplement(self, num: int):
        return 2**(len(bin(num))-2)-num-1
