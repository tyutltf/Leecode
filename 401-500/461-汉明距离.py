# -*- encoding: utf-8 -*-
"""
@File    :   461-汉明距离.py
@Time    :   2021/07/06 22:09:41
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
"""
# here put the import lib
"""
两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。

给你两个整数 x 和 y，计算并返回它们之间的汉明距离。

 

示例 1：

输入：x = 1, y = 4
输出：2
解释：
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
上面的箭头指出了对应二进制位不同的位置。
示例 2：

输入：x = 3, y = 1
输出：1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/hamming-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
可能日常很多人了解的异或操作就是

0⊕0=0
0⊕1=1
1⊕0=1
1⊕1=0
但如果仔细学习就会了解对于两个数字的异或结果，其实是转化为二进制后按位比较的。
如上方示例的说明
1 ^ 4 后由于第一位和第三位(从低位到高位/右到左)不同，所以结果是0101结果为5，所以1^ 4 = 5
那么，我们只需要先将两数异或后，获取哪些位数为1代表这两个数该位上的值不同，就是结果。

"""


class Solution:
    def hammingDistance(self, x, y):
        return bin(x ^ y).count("1")
