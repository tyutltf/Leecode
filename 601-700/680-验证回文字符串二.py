# -*- encoding: utf-8 -*-
'''
@File    :   680-验证回文字符串二.py
@Time    :   2021/08/18 20:06:19
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
'''
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:

输入: s = "aba"
输出: true
示例 2:

输入: s = "abca"
输出: true
解释: 你可以删除c字符。
示例 3:

输入: s = "abc"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def validPalindrome(self, s: str):
        li = 0
        ri = len(s)-1
        while li < ri:
            if s[li] == s[ri]:
                li += 1
                ri -= 1
            else:
                # 删除左边或者删除右边 两种情况都要考虑
                print(s[li:ri])
                print(s[li+1:ri+1])
                return self.is_palindrome(s[li:ri]) or self.is_palindrome(s[li+1:ri+1])
        return True

    def is_palindrome(self, s):
        if s == s[::-1]:
            return True
        else:
            return False


obj = Solution()
# s = 'abeca'
s = 'deeee'
print(obj.validPalindrome(s))
