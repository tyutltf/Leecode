# -*- encoding: utf-8 -*-
'''
@File    :   709-转换成小写字母.py
@Time    :   2021/12/02 19:55:21
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
'''
给你一个字符串 s ，将该字符串中的大写字母转换成相同的小写字母，返回新的字符串。

示例 1：

输入：s = "Hello"
输出："hello"
示例 2：

输入：s = "here"
输出："here"
示例 3：

输入：s = "LOVELY"
输出："lovely"
 

提示：

1 <= s.length <= 100
s 由 ASCII 字符集中的可打印字符组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/to-lower-case
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def toLowerCase(self, s: str):
        # * return s.lower()
        s = list(s)
        for i in range(len(s)):
            if "A" <= s[i] <= "Z":
                s[i] = chr(ord(s[i])+ord("a")-ord("A"))
        return "".join(s)


object = Solution()
s = 'AGHhsghdDS'
print(object.toLowerCase(s))
