# -*- encoding: utf-8 -*-
"""
@File    :   58-最后一个单词的长度.py
@Time    :   2023/06/09 20:11:02
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@Lic
"""

"""
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。

示例:

输入: "Hello World"
输出: 5
"""


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        tail = len(s) - 1
        while tail >= 0 and s[tail] == " ":
            tail -= 1
        while tail >= 0 and s[tail] != " ":
            count += 1
            tail -= 1
        return count
        # list=s.split(' ')
        # return len(list[-1])
        # 这种写法没有考虑字符串结尾是空格的情况


object = Solution()
s = "a "
result = object.lengthOfLastWord(s)
print(result)
