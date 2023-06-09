# -*- encoding: utf-8 -*-
"""
@File    :   3-无重复字符的最长子串.py
@Time    :   2023/06/09 20:11:02
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
"""

"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"


s=input('请输入字符串:')
print(s)
for i in range(len(s)//2+1):
    print(i)
for j in range(len(s)-1,len(s)//2,-1):
    print(j)


def longestPalindrome(s):
    maxl, lens = 1, len(s)
    for i in range(lens):
        j = 1
        while i - j >= 0 and i + j < lens:
            if s[i - j] != s[i + j]:
                break
            j += 1
        if 2 * (j - 1) + 1 > maxl:
            maxl = 2 * (j - 1) + 1
        j = 0
        while i - j >= 0 and i + j + 1 < lens:
            if s[i - j] != s[i + j + 1]:
                break
            j += 1
        if 2 * (j - 1) + 2 > maxl:
            maxl = 2 * (j - 1) + 2
    return maxl


if __name__ == '__main__':
    s = 'asdwabccbaufyioop'
    print(longestPalindrome(s))
"""

s = "qwerabcbadef"
k = len(s)  # 计算字符串的长度
matrix = [[0 for i in range(k)] for i in range(k)]  # 初始化n*n的列表
logestSubStr = ""  # 存储最长回文子串
logestLen = 0  # 最长回文子串的长度

for j in range(0, k):
    for i in range(0, j + 1):
        if j - i <= 1:
            if s[i] == s[j]:
                matrix[i][j] = 1  # 此时f(i,j)置为true
                if logestLen < j - i + 1:  # 将s[i:j]的长度与当前的回文子串的最长长度相比
                    logestSubStr = s[i: j + 1]  # 取当前的最长回文子串
                    logestLen = j - i + 1  # 当前最长回文子串的长度
        else:
            if s[i] == s[j] and matrix[i + 1][j - 1]:  # 判断
                matrix[i][j] = 1
                if logestLen < j - i + 1:
                    logestSubStr = s[i: j + 1]
                    logestLen = j - i + 1
print(logestSubStr)
print(logestLen)
