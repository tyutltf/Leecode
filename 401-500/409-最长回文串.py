# -*- encoding: utf-8 -*-
'''
@File    :   409-最长回文串.py
@Time    :   2021/06/16 10:12:42
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
from collections import Counter
'''
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。

示例 1:

输入:
"abccccdd"

输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。

'''


class Solution:
    def longestPalindrome(self, s: str):
        if not s:
            return 0
        ct = Counter(s)
        # 统计每个字符的个数
        res = list(ct.values())
        length = 0
        temp = 0
        # 是偶数直接相加 是奇数-1再相加
        for i in res:
            if i % 2 == 0:
                length += i
            else:
                temp = 1
                i = i - 1
                length += i
        length += temp
        return length


s = 'ccc'
obj = Solution()
print(obj.longestPalindrome(s))
