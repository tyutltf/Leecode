# -*- encoding: utf-8 -*-
"""
@File    :   844-比较含退格的字符串.py
@Time    :   2023/08/03 14:17:19
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
"""
# here put the import lib

"""
给定 s 和 t 两个字符串，当它们分别被输入到空白的文本编辑器后，如果两者相等，返回 true 。# 代表退格字符。

注意：如果对空文本输入退格字符，文本继续为空。


示例 1：

输入：s = "ab#c", t = "ad#c"
输出：true
解释：s 和 t 都会变成 "ac"。
示例 2：

输入：s = "ab##", t = "c#d#"
输出：true
解释：s 和 t 都会变成 ""。
示例 3：

输入：s = "a#c", t = "b"
输出：false
解释：s 会变成 "c"，但 t 仍然是 "b"。


提示：

1 <= s.length, t.length <= 200
s 和 t 只含有小写字母以及字符 '#'

"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_res = self.get_real_str(s)
        t_res = self.get_real_str(t)
        if s_res == t_res:
            return True
        return False

    def get_real_str(self, s: str):
        '''
        s和t分别对应一个栈。

        遇到普通字符，即入栈；如遇到 # 而且栈不为空，即出栈。

        最终比较两个栈内元素是否相等即可。
        '''
        stack = []
        for x in s:
            if x == "#":
                if len(stack):
                    stack.pop()
                continue
            stack.append(x)
        return stack


obj = Solution()
s = "ab##"
t = "c#d#"
print(obj.backspaceCompare(s, t))
