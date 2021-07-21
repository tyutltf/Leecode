# -*- encoding: utf-8 -*-
'''
@File    :   500-键盘行.py
@Time    :   2021/07/21 20:55:38
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
from typing import List
'''
给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。

美式键盘 中：

第一行由字符 "qwertyuiop" 组成。
第二行由字符 "asdfghjkl" 组成。
第三行由字符 "zxcvbnm" 组成。

示例 1：

输入：words = ["Hello","Alaska","Dad","Peace"]
输出：["Alaska","Dad"]
示例 2：

输入：words = ["omk"]
输出：[]
示例 3：

输入：words = ["adsdf","sfd"]
输出：["adsdf","sfd"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/keyboard-row
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 构建字典的步骤
# a1 = 'qwertyuiopQWERTYUIOP'
# a2 = 'asdfghjklASDFGHJKL'
# a3 = 'zxcvbnmZXCVBNM'
# res = {}
# a = dict(zip(list(a1), len(a1)*[1]))
# res.update(a)
# b = dict(zip(list(a2), len(a2)*[2]))
# res.update(b)
# c = dict(zip(list(a3), len(a3)*[3]))
# res.update(c)
# print(res)


class Solution:
    def findWords(self, words: List[str]):
        dict = {'q': 1, 'w': 1, 'e': 1, 'r': 1, 't': 1, 'y': 1, 'u': 1, 'i': 1, 'o': 1, 'p': 1, 'Q': 1, 'W': 1, 'E': 1, 'R': 1, 'T': 1, 'Y': 1, 'U': 1, 'I': 1, 'O': 1, 'P': 1, 'a': 2, 's': 2, 'd': 2, 'f': 2, 'g': 2, 'h': 2,
                'j': 2, 'k': 2, 'l': 2, 'A': 2, 'S': 2, 'D': 2, 'F': 2, 'G': 2, 'H': 2, 'J': 2, 'K': 2, 'L': 2, 'z': 3, 'x': 3, 'c': 3, 'v': 3, 'b': 3, 'n': 3, 'm': 3, 'Z': 3, 'X': 3, 'C': 3, 'V': 3, 'B': 3, 'N': 3, 'M': 3}
        res = []
        for word in words:
            temp = []
            for i in word:
                num = dict.get(i)
                if num not in temp:
                    temp.append(num)
                    if len(temp) != 1:
                        is_in = 0
                    else:
                        is_in = 1
            if is_in:
                res.append(word)
        return res

        # 或者也可以用集合的办法
        # set1 = set('qwertyuiop')
        # set2 = set('asdfghjkl')
        # set3 = set('zxcvbnm')
        # res = []
        # for i in words:
        #     x = i.lower()
        #     setx = set(x)
        #     if setx<=set1 or setx<=set2 or setx<=set3:
        #         res.append(i)
        # return res


words = ["Hello", "Alaska", "Dad", "Peace"]
obj = Solution()
print(obj.findWords(words))
