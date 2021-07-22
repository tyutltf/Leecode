# -*- encoding: utf-8 -*-
'''
@File    :   507-完美数.py
@Time    :   2021/07/22 22:31:26
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
import math
'''
对于一个 正整数，如果它和除了它自身以外的所有 正因子 之和相等，我们称它为 「完美数」。

给定一个 整数 n， 如果是完美数，返回 true，否则返回 false

示例 1：

输入：28
输出：True
解释：28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, 和 14 是 28 的所有正因子。
示例 2：

输入：num = 6
输出：true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/perfect-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def checkPerfectNumber(self, num: int):
        # ?return num in {6, 28, 496, 8128, 33550336}

        # 对于数字1:直接返回`False`
        if num == 1:
            return False
        # 计数从1开始
        total = 1
        # 我们只需要判断`2-int(sqrt(num))+1`的数，全部累加
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                # 这里total要加上i和num // i
                total += (i + num // i)
        return total == num
