# -*- encoding: utf-8 -*-
"""
@File    :   14-最长公共前缀.py
@Time    :   2023/06/09 20:11:02
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
"""
"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        if len(strs) == 0:
            return ""
        for each in zip(*strs):  # zip()函数用于将可迭代对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
            if len(set(each)) == 1:  # 利用集合创建一个无序不重复元素集
                res += each[0]
            else:
                return res
        return res


obj = Solution()
strs = ["ltf123", "ltf12qwrd", "ltf1wrsd", "ltfagx", "ltf123456", "lt"]
strs1 = ["qwefgu", "qwe134769", "jfh", "qwety"]
print(obj.longestCommonPrefix(strs))
print(obj.longestCommonPrefix(strs1))
