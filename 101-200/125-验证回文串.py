'''
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false

'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        s = s.lower()
        for i in s:
            if i in 'abcdefghijklmnopqrstuvwxyz0123456789':
                new_s += i
        print(new_s)
        s_new = new_s[::-1]
        if new_s == s_new:
            return True
        else:
            return False


object = Solution()
s = "A man, a plan, a canal: Panama"
print(object.isPalindrome(s))
