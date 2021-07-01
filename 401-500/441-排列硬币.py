# -*- encoding: utf-8 -*-
'''
@File    :   441-排列硬币.py
@Time    :   2021/07/01 22:11:55
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib

import math
'''
你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。

给定一个数字 n，找出可形成完整阶梯行的总行数。

n 是一个非负整数，并且在32位有符号整型的范围内。

示例 1:

n = 5

硬币可排列成以下几行:
¤
¤ ¤
¤ ¤

因为第三行不完整，所以返回2.
示例 2:

n = 8

硬币可排列成以下几行:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

因为第四行不完整，所以返回3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/arranging-coins
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
k 一定比根号2n 小
k(k + 1) <= 2n
'''


class Solution:
    def arrangeCoins(self, n: int):
        k = int(math.sqrt(2 * n))
        while k * (k + 1) > 2 * n:
            # 不停缩小k值
            k -= 1
        return k


obj = Solution()
print(obj.arrangeCoins(10))
