# -*- encoding: utf-8 -*-
'''
@File    :   338-比特位计数.py
@Time    :   2021/07/15 23:21:37
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
'''
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:

输入: 2
输出: [0,1,1]
示例 2:

输入: 5
输出: [0,1,1,2,1,2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/counting-bits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def countBits(self, n: int):
        temp = [i for i in range(n+1)]
        return [bin(i).count('1') for i in temp]

        # 动态规划法 看不懂
        # res = [0] * (n + 1)
        # for i in range(1, n + 1):
        #     res[i] = res[i >> 1] + (i & 1)
        # return res


obj = Solution()
print(obj.countBits(5))
