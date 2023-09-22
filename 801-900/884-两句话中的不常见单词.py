# -*- encoding: utf-8 -*-
"""
@File    :   884-两句话中的不常见单词.py
@Time    :   2023/09/22 20:26:30
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
"""
from collections import Counter

# here put the import lib
from typing import List

"""
句子 是一串由空格分隔的单词。每个 单词 仅由小写字母组成。

如果某个单词在其中一个句子中恰好出现一次，在另一个句子中却 没有出现 ，那么这个单词就是 不常见的 。

给你两个 句子 s1 和 s2 ，返回所有 不常用单词 的列表。返回列表中单词可以按 任意顺序 组织。


示例 1：

输入：s1 = "this apple is sweet", s2 = "this apple is sour"
输出：["sweet","sour"]
示例 2：

输入：s1 = "apple apple", s2 = "banana"
输出：["banana"]


提示：

1 <= s1.length, s2.length <= 200
s1 和 s2 由小写英文字母和空格组成
s1 和 s2 都不含前导或尾随空格
s1 和 s2 中的所有单词间均由单个空格分隔
"""


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res = s1 + " " + s2
        res_list = res.split(" ")
        char_count = Counter(res_list)  # 使用 Counter 统计字符出现次数

        # 找到出现次数为 1 的字符
        single_occurrence_chars = [
            char for char, count in char_count.items() if count == 1
        ]

        return single_occurrence_chars


obj = Solution()
s1 = "this apple is sweet"
s2 = "this apple is sour"
print(obj.uncommonFromSentences(s1, s2))
