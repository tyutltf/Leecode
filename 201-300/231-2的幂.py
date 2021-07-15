# -*- encoding: utf-8 -*-
'''
@File    :   231-2的幂.py
@Time    :   2021/07/15 20:12:55
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib

'''
给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。

如果存在一个整数 x 使得 n == 2x ，则认为 n 是 2 的幂次方。

 

示例 1：

输入：n = 1
输出：true
解释：20 = 1
示例 2：

输入：n = 16
输出：true
解释：24 = 16
示例 3：

输入：n = 3
输出：false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/power-of-two
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


解题思路：
若 n = 2^x 且 xx 为自然数（即 nn 为 22 的幂），则一定满足以下条件：
恒有 n & (n - 1) == 0，这是因为：
nn 二进制最高位为 11，其余所有位为 00；
n - 1n−1 二进制最高位为 00，其余所有位为 11；
一定满足 n > 0。
因此，通过 n > 0 且 n & (n - 1) == 0 即可判定是否满足 n = 2^xn=2

作者：jyd
链接：https://leetcode-cn.com/problems/power-of-two/solution/power-of-two-er-jin-zhi-ji-jian-by-jyd/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


class Solution:
    def isPowerOfTwo(self, n: int):
        return n > 0 and n & (n - 1) == 0
