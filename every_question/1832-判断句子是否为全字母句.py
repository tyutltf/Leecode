# -*- encoding: utf-8 -*-
'''
@File    :   1832-判断句子是否为全字母句.py
@Time    :   2022/12/13 18:40:56
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
'''
全字母句 指包含英语字母表中每个字母至少一次的句子。

给你一个仅由小写英文字母组成的字符串 sentence ，请你判断 sentence 是否为 全字母句 。

如果是，返回 true ；否则，返回 false 。

示例 1：

输入：sentence = "thequickbrownfoxjumpsoverthelazydog"
输出：true
解释：sentence 包含英语字母表中每个字母至少一次。
示例 2：

输入：sentence = "leetcode"
输出：false
'''


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # 去重长度是否是26 是=true、不是=false
        flag = len(set(sentence))
        if flag == 26:
            return True
        else:
            return False


if __name__ == '__main__':
    obj = Solution()
    sentence = ''
    print(obj.checkIfPangram(sentence))