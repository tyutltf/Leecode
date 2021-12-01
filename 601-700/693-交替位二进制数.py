# -*- encoding: utf-8 -*-
'''
@File    :   693-交替位二进制数.py
@Time    :   2021/08/19 20:29:01
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
'''
给定一个正整数，检查它的二进制表示是否总是 0、1 交替出现：
换句话说，就是二进制表示中相邻两位的数字永不相同。

示例 1：

输入：n = 5
输出：true
解释：5 的二进制表示是：101
示例 2：

输入：n = 7
输出：false
解释：7 的二进制表示是：111.
示例 3：

输入：n = 11
输出：false
解释：11 的二进制表示是：1011.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-number-with-alternating-bits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def hasAlternatingBits(self, n: int):
        bin_str = bin(n)[2:]
        # print(bin_str)
        # a, b = 0, 1
        # while a <= len(bin_str) and b < len(bin_str):
        #     if bin_str[a] != '1':
        #         return False
        #     elif bin_str[b] != '0':
        #         return False
        #     a += 2
        #     b += 2
        # return True

        return all(bin_str[i-1] != bin_str[i] for i in range(1, len(bin_str)))


obj = Solution()
print(obj.hasAlternatingBits(5))
