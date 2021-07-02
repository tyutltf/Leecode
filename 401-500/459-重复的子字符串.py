# -*- encoding: utf-8 -*-
'''
@File    :   459-重复的子字符串.py
@Time    :   2021/07/02 20:20:55
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib

'''
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。

示例 1:

输入: "abab"

输出: True

解释: 可由子字符串 "ab" 重复两次构成。
示例 2:

输入: "aba"

输出: False
示例 3:

输入: "abcabcabcabc"

输出: True

解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)


'''

'''
假设 s 可由 子串 x 重复 n 次构成，即 s = nx
则有 s+s = 2nx
移除 s+s 开头和结尾的字符，变为 (s+s)[1:-1]，则破坏了开头和结尾的子串 x
此时只剩 2n-2 个子串
若 s 在 (s+s)[1:-1] 中，则有 2n-2 >= n，即 n >= 2
即 s 至少可由 x 重复 2 次构成
否则，n < 2，n 为整数，只能取 1，说明 s 不能由其子串重复多次构成

'''


class Solution:
    def repeatedSubstringPattern(self, s: str):
        return s in (s+s)[1:-1]


obj = Solution()
obj.repeatedSubstringPattern("abcabcabcabc")
