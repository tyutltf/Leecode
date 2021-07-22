# -*- encoding: utf-8 -*-
'''
@File    :   520-检测大写字母.py
@Time    :   2021/07/22 22:51:37
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
'''
给定一个单词，你需要判断单词的大写使用是否正确。

我们定义，在以下情况时，单词的大写用法是正确的：

全部字母都是大写，比如"USA"。
单词中所有字母都不是大写，比如"leetcode"。
如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。
否则，我们定义这个单词没有正确使用大写字母。

示例 1:

输入: "USA"
输出: True
示例 2:

输入: "FlaG"
输出: False

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/detect-capital
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def detectCapitalUse(self, word: str):
        # ?65～90为26个大写英文字母，97～122号为26个小写英文字母
        res = 0
        # 求单个字母的ascll码 是小写字母+1 否则+0
        for i in word:
            temp = ord(i)
            if temp >= 97:
                res += 1
            else:
                res += 0
        # 开始判断res 三种情况全大写 全小写 或者首字母大写 其余返回faslse
        if res == 0 or res == len(word):
            return True
        elif res == len(word)-1:
            if ord(word[0]) <= 90:
                return True
            else:
                return False
        else:
            return False


object = Solution()
word = 'g'
print(object.detectCapitalUse(word))
