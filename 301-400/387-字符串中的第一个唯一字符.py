# -*- encoding: utf-8 -*-
'''
@File    :   387-字符串中的第一个唯一字符.py
@Time    :   2021/06/08 14:31:35
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
from collections import Counter
'''
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

示例：

s = "leetcode"
返回 0

s = "loveleetcode"
返回 2

'''


class Solution:
    def firstUniqChar(self, s: str):
        d = Counter(s)
        for i, j in enumerate(s):
            if d[j] == 1:
                return i
        return -1
        # d = {}
        # length = len(s)
        # for i in range(length):
        #     if s[i] not in d:
        #         d[s[i]] = i
        #     else:
        #         d[s[i]] = length + 1
        # print(d)
        # ret = min(d.values())
        # return -1 if ret > length else ret


obj = Solution()
print(obj.firstUniqChar('aabb'))
print(obj.firstUniqChar('loveleetcode'))
