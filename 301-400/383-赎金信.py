# -*- encoding: utf-8 -*-
'''
@File    :   383-赎金信.py
@Time    :   2021/06/08 14:12:49
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
import collections
'''
给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串 ransom 能不能由第二个字符串 magazines 里面的字符构成。如果可以构成，返回 true ；否则返回 false。

(题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。杂志字符串中的每个字符只能在赎金信字符串中使用一次。)

 

示例 1：

输入：ransomNote = "a", magazine = "b"
输出：false
示例 2：

输入：ransomNote = "aa", magazine = "ab"
输出：false
示例 3：

输入：ransomNote = "aa", magazine = "aab"
输出：true
 

提示：

你可以假设两个字符串均只含有小写字母。

'''


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str):
        # 自己想法 俩列表 遍历即可
        ran = list(ransomNote)
        mag = list(magazine)
        for i in ran:
            if i in mag:
                mag.remove(i)
            else:
                return False
        return True
        # 借鉴 collections 求差集
        # hash_table_m = collections.Counter(magazine)
        # hash_table_r = collections.Counter(ransomNote)
        # print(hash_table_r - hash_table_m)
        # return not hash_table_r - hash_table_m


obj = Solution()
print(obj.canConstruct('aaaxc', 'axcaxcazaz'))
