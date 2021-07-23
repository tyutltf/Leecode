# -*- encoding: utf-8 -*-
'''
@File    :   521-最长特殊子序列.py
@Time    :   2021/07/23 20:57:10
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
'''
给你两个字符串，请你从这两个字符串中找出最长的特殊序列。

「最长特殊序列」定义如下：该序列为某字符串独有的最长子序列（即不能是其他字符串的子序列）。

子序列 可以通过删去字符串中的某些字符实现，但不能改变剩余字符的相对顺序。空序列为所有字符串的子序列，任何字符串为其自身的子序列。

输入为两个字符串，输出最长特殊序列的长度。如果不存在，则返回 -1。


示例 1：

输入: "aba", "cdc"
输出: 3
解释: 最长特殊序列可为 "aba" (或 "cdc")，两者均为自身的子序列且不是对方的子序列。
示例 2：

输入：a = "aaa", b = "bbb"
输出：3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-uncommon-subsequence-i
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

解题思路
本题简直是脑筋急转弯，两种大情况：一是两个字符串长度不同，那么长的肯定不是短的子序列；
另外一种大情况是长度相同，或者相等返回-1，或者当两个字符串不相等时那么两个子串肯定不互为子序列

'''


class Solution:
    def findLUSlength(self, a: str, b: str):
        na, nb = len(a), len(b)
        # 1.当两个序列长度不一致时，最长的序列即为特殊序列，因为肯定不为另一个序列的子序列
        if na != nb:
            return max(na, nb)
        # 2.当两个序列长度一致时，使用滑动窗口判断
        if a == b:  # 两个字符串相等时
            return -1
        else:
            return na  # 当两个字符串不相等时，其中一个字符串肯定不是另外一个字符串的子序列
