# -*- encoding: utf-8 -*-
"""
@File    :   66-加一.py
@Time    :   2023/06/09 20:11:02
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@Lic
"""

"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
"""


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        result = []
        num = 0
        # 先转换成整数在做。。
        for i in range(length):
            num += digits[i] * (10 ** (length - 1 - i))
        num += 1
        str_num = str(num)
        for i in str_num:
            result.append(int(i))

        return result


object = Solution()
results = object.plusOne([1, 2, 9, 9])
print(results)
