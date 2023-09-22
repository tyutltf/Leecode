# -*- encoding: utf-8 -*-
"""
@File    :   888-公平的糖果交换.py
@Time    :   2023/09/22 21:53:15
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
"""
# here put the import lib
from typing import List

"""
爱丽丝和鲍勃拥有不同总数量的糖果。给你两个数组 aliceSizes 和 bobSizes ，aliceSizes[i] 是爱丽丝拥有的第 i 盒糖果中的糖果数量，bobSizes[j] 是鲍勃拥有的第 j 盒糖果中的糖果数量。

两人想要互相交换一盒糖果，这样在交换之后，他们就可以拥有相同总数量的糖果。一个人拥有的糖果总数量是他们每盒糖果数量的总和。

返回一个整数数组 answer，其中 answer[0] 是爱丽丝必须交换的糖果盒中的糖果的数目，answer[1] 是鲍勃必须交换的糖果盒中的糖果的数目。如果存在多个答案，你可以返回其中 任何一个 。题目测试用例保证存在与输入对应的答案。


示例 1：

输入：aliceSizes = [1,1], bobSizes = [2,2]
输出：[1,2]
示例 2：

输入：aliceSizes = [1,2], bobSizes = [2,3]
输出：[1,2]
示例 3：

输入：aliceSizes = [2], bobSizes = [1,3]
输出：[2,3]
示例 4：

输入：aliceSizes = [1,2,5], bobSizes = [2,4]
输出：[5,4]
"""


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_sum = sum(aliceSizes)
        bob_sum = sum(bobSizes)
        # 求差值
        diff = alice_sum - bob_sum
        print(diff)
        # 求互换的两个数之间的值 diff//2
        diff_2 = diff // 2
        print(diff_2)
        for i in aliceSizes:
            if i - diff_2 in bobSizes:
                res = [i, i - diff_2]
        return res


obj = Solution()
aliceSizes = [2]
bobSizes = [1, 3]
print(obj.fairCandySwap(aliceSizes, bobSizes))
