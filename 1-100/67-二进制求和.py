# -*- encoding: utf-8 -*-
"""
@File    :   67-二进制求和.py
@Time    :   2023/06/09 20:11:02
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@Lic
"""

"""
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
"""


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # return bin(int(a,2)+int(b,2))[2:]
        la, lb = len(a), len(b)
        i, j = la - 1, lb - 1
        cin = 0
        result = ""
        while (i >= 0) and (j >= 0):
            tmp = (cin + int(a[i]) + int(b[j])) % 2
            cin = (cin + int(a[i]) + int(b[j])) // 2
            result = str(tmp) + result
            i -= 1
            j -= 1
        if i < 0 and j >= 0:
            while j >= 0:
                tmp = (cin + int(b[j])) % 2
                cin = (cin + int(b[j])) // 2
                result = str(tmp) + result
                j -= 1
        elif i >= 0 and j < 0:
            while i >= 0:
                tmp = (cin + int(a[i])) % 2
                cin = (cin + int(a[i])) // 2
                result = str(tmp) + result
                i -= 1
        if cin == 1:
            result = "1" + result
        return result


object = Solution()
result = object.addBinary("101010", "11101")
print(result)
