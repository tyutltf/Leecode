# -*- encoding: utf-8 -*-
'''
@File    :   557-反转字符串中的单词三.py
@Time    :   2021/07/23 21:46:41
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
'''
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例：

输入："Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"
 

提示：

在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def reverseWords(self, s: str):
        s_list = s.split(' ')
        s_list = [i[::-1] for i in s_list]

        return ' '.join(s_list)

        # ? 两次切片 时间 20ms 超越 100%
        # return " ".join(s.split(" ")[::-1])[::-1]


obj = Solution()
s = "Let's take LeetCode contest"
print(obj.reverseWords(s))
