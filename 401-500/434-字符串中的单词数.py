# -*- encoding: utf-8 -*-
'''
@File    :   434-字符串中的单词数.py
@Time    :   2021/07/01 21:04:39
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
'''
统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。

请注意，你可以假定字符串里不包括任何不可打印的字符。

示例:

输入: "Hello, my name is John"
输出: 5
解释: 这里的单词是指连续的不是空格的字符，所以 "Hello," 算作 1 个单词。

'''


class Solution:
    def countSegments(self, s: str):
        res = 0
        temp = s.split(' ')
        for word in temp:
            if word != '':
                res += 1
        return res


obj = Solution()
print(obj.countSegments("Hello, my name is John"))
