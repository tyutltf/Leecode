'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''
'''
s='pwwkew'
max_number = 0
number = 0
test = ''
for i in s:
    #如果i不在test字符串里面，字符串test添加这个字符，number+1
    if i not in test:
        test += i
        number += 1
        global s1
        s1=test
    else:  #i在test字符串里
        if number >= max_number:
            max_number = number
        index = test.index(i)
        test = test[(index+1):] + i
        number=len(test)
    if number > max_number:
        max_number = number
print(s1)
print(max_number)
'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # s='abcabcbb'
        max_number = 0
        number = 0
        test = ''
        for i in s:
            # 如果i不在test字符串里面，字符串test添加这个字符，number+1
            if i not in test:
                test += i
                number += 1
                global s1
                s1 = test
            else:  # i在test字符串里
                if number >= max_number:
                    max_number = number
                index = test.index(i)
                test = test[(index+1):] + i
                number = len(test)
            if number > max_number:
                max_number = number
        return max_number


obj = Solution()
obj.lengthOfLongestSubstring('pwwkew')
