# -*- encoding: utf-8 -*-
'''
@File    :   720-词典中最长的单词.py
@Time    :   2022/01/05 20:29:50
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
from typing import List
'''
给出一个字符串数组words组成的一本英语词典。从中找出最长的一个单词，该单词是由words词典中其他单词逐步添加一个字母组成。若其中有多个可行的答案，则返回答案中字典序最小的单词。

若无答案，则返回空字符串。

示例 1：

输入：
words = ["w","wo","wor","worl", "world"]
输出："world"
解释
单词"world"可由"w", "wo", "wor", 和 "worl"添加一个字母组成。
示例 2：

输入：
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
输出："apple"
解释：
"apply"和"apple"都能由词典中的单词组成。但是"apple"的字典序小于"apply"。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-word-in-dictionary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
对于每个单词，我们可以检查它的全部前缀是否存在，可以通过 Set 数据结构来加快查找

算法：

当我们找到一个单词它的长度更长且它的全部前缀都存在，我们将更改答案。
或者，我们可以事先将单词排序，这样当我们找到一个符合条件的单词就可以认定它是答案。

'''


class Solution:
    def longestWord(self, words: List[str]) -> str:
        wordset = set(words)
        words.sort(key=lambda c: (-len(c), c))
        for word in words:
            if all(word[:k] in wordset for k in range(1, len(word))):
                return word

        return ""


obj = Solution()
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
print(obj.longestWord(words))
