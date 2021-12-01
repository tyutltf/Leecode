# -*- encoding: utf-8 -*-
'''
@File    :   696-计算二进制子串.py
@Time    :   2021/12/01 19:54:53
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
'''
给定一个字符串 s，计算具有相同数量 0 和 1 的非空（连续）子字符串的数量，并且这些子字符串中的所有 0 和所有 1 都是连续的。

重复出现的子串要计算它们出现的次数。

 

示例 1 :

输入: "00110011"
输出: 6
解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。

请注意，一些重复出现的子串要计算它们出现的次数。

另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。
示例 2 :

输入: "10101"
输出: 4
解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。
 

提示：

s.length 在1到50,000之间。
s 只包含“0”或“1”字符。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-binary-substrings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def countBinarySubstrings(self, s: str):
        seq0, seq1 = 0, 1
        res = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                seq1 += 1
            else:
                res += min(seq0, seq1)
                seq0 = seq1
                seq1 = 1
        res += min(seq0, seq1)
        return res


obj = Solution()
s = '00110011'
print(obj.countBinarySubstrings(s))
