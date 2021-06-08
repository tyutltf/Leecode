# -*- encoding: utf-8 -*-
'''
@File    :   389-找不同.py
@Time    :   2021/06/08 15:05:27
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
import collections
'''
给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。

 

示例 1：

输入：s = "abcd", t = "abcde"
输出："e"
解释：'e' 是那个被添加的字母。
示例 2：

输入：s = "", t = "y"
输出："y"
示例 3：

输入：s = "a", t = "aa"
输出："a"
示例 4：

输入：s = "ae", t = "aea"
输出："a"
 

提示：

0 <= s.length <= 1000
t.length == s.length + 1
s 和 t 只包含小写字母

'''


class Solution:
    def findTheDifference(self, s: str, t: str):
        # 俩循环 列表
        # a = list(s)
        # b = list(t)
        # for i in a:
        #     if i in b:
        #         b.remove(i)
        # return b[0]

        # 统计字符串每个字符的字数 不相等的即是目标元素
        countS = collections.Counter(s)
        countT = collections.Counter(t)
        for val in countT:
            if countT[val] != countS[val]:
                return val


obj = Solution()
print(obj.findTheDifference('abcd', 'abcde'))
