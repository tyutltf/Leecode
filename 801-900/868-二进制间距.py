# -*- encoding: utf-8 -*-
"""
@File    :   868-二进制间距.py
@Time    :   2023/08/08 10:28:50
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
"""
# here put the import lib

"""
给定一个正整数 n，找到并返回 n 的二进制表示中两个 相邻 1 之间的 最长距离 。如果不存在两个相邻的 1，返回 0 。

如果只有 0 将两个 1 分隔开（可能不存在 0 ），则认为这两个 1 彼此 相邻 。两个 1 之间的距离是它们的二进制表示中位置的绝对差。例如，"1001" 中的两个 1 的距离为 3 。


示例 1：

输入：n = 22
输出：2
解释：22 的二进制是 "10110" 。
在 22 的二进制表示中，有三个 1，组成两对相邻的 1 。
第一对相邻的 1 中，两个 1 之间的距离为 2 。
第二对相邻的 1 中，两个 1 之间的距离为 1 。
答案取两个距离之中最大的，也就是 2 。
示例 2：

输入：n = 8
输出：0
解释：8 的二进制是 "1000" 。
在 8 的二进制表示中没有相邻的两个 1，所以返回 0 。
示例 3：

输入：n = 5
输出：2
解释：5 的二进制是 "101" 。


提示：

1 <= n <= 109
"""


class Solution:
    def binaryGap(self, n: int) -> int:
        # # 获取二进制并替换 '0b'
        # n_two = list(bin(n).replace('0b', ''))
        # # 获取列表所有1的下标
        # indices = [index for index, value in enumerate(n_two) if value == '1']
        # if len(indices) >= 2:
        #     # 求下标之间的差值绝对值，并返回最大值
        #     differences = [abs(indices[i+1] - indices[i]) for i in range(len(indices)-1)]
        #     return max(differences)
        # else:
        #     return 0

        # * 贪心法
        # * 思路：贪心法
        # * 找到1的下标的同时，同时保存上一个1的下标，然后进行作差求解。
        cur, pre, maxs = 0, n, 0
        while n != 0:
            # 如果当前位为1
            if n & 1 == 1:
                # 贪心
                maxs = max(maxs, cur - pre)
                pre = cur
            cur = cur + 1
            n = n >> 1
        return maxs


obj = Solution()
n = 22
print(obj.binaryGap(n))
