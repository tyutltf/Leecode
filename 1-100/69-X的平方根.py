# -*- encoding: utf-8 -*-
"""
@File    :   69-X的平方根.py
@Time    :   2023/06/09 20:11:02
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@Lic
"""

"""
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。
"""


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        r = x
        while r > x / r:
            r = (r + x / r) // 2
            print(r)
        return int(r)


object = Solution()
print(object.mySqrt(9))
print(9 / 9)  # 除法
print(9 // 4)  # 整除
