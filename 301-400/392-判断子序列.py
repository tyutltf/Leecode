# -*- encoding: utf-8 -*-
'''
@File    :   392-判断子序列.py
@Time    :   2021/06/10 20:47:08
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib

'''
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

进阶：

如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

致谢：

特别感谢 @pbrother 添加此问题并且创建所有测试用例。

 

示例 1：

输入：s = "abc", t = "ahbgdc"
输出：true
示例 2：

输入：s = "axc", t = "ahbgdc"
输出：false

这是一道简单的指针问题，首先我们for循环t，然后创建一个ret=0的指针指在s[ret]的位置。

当循环t时发现与s[ret]相等，那我们就将ret的指针+=1

当循环结束后，如果ret的指针不等于len(s)表示没有在t中找到所有的s。返回False即可。

'''


class Solution:
    def isSubsequence(self, s: str, t: str):
        length = len(s)
        ret = 0
        for i in t:
            if ret == length:
                return True
            elif i == s[ret]:
                ret += 1
        return True if ret == length else False
