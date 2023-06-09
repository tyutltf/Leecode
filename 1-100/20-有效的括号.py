# -*- encoding: utf-8 -*-
"""
@File    :   20-有效的括号.py
@Time    :   2023/06/09 20:11:02
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
"""
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
"""

s = input("请输入字符串:")
stack = []
map = {")": "(", "]": "[", "}": "{"}
for char in s:
    if char not in map:
        stack.append(char)
    elif not stack or map[char] != stack.pop():
        print(False)
print(not stack)
