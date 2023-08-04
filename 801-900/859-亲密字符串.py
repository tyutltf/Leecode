# -*- encoding: utf-8 -*-
"""
@File    :   859-亲密字符串.py
@Time    :   2023/08/03 14:46:30
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
"""
# here put the import lib

"""
给你两个字符串 s 和 goal ，只要我们可以通过交换 s 中的两个字母得到与 goal 相等的结果，就返回 true ；否则返回 false 。

交换字母的定义是：取两个下标 i 和 j （下标从 0 开始）且满足 i != j ，接着交换 s[i] 和 s[j] 处的字符。

例如，在 "abcd" 中交换下标 0 和下标 2 的元素可以生成 "cbad" 。


示例 1：

输入：s = "ab", goal = "ba"
输出：true
解释：你可以交换 s[0] = 'a' 和 s[1] = 'b' 生成 "ba"，此时 s 和 goal 相等。
示例 2：

输入：s = "ab", goal = "ab"
输出：false
解释：你只能交换 s[0] = 'a' 和 s[1] = 'b' 生成 "ba"，此时 s 和 goal 不相等。
示例 3：

输入：s = "aa", goal = "aa"
输出：true
解释：你可以交换 s[0] = 'a' 和 s[1] = 'a' 生成 "aa"，此时 s 和 goal 相等。


提示：

1 <= s.length, goal.length <= 2 * 104
s 和 goal 由小写英文字母组成
"""

"""

返回true情况： 大条件：len(A) == len(B) 一：有两个不同地方(i,j)，且A[i]=B[j],A[j]=B[i] 二：完全相同，一个数组中存在重复数字

"""


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        index = []
        if len(A) == len(B):
            for i in range(len(A)):
                if A[i] != B[i]:
                    index.append(i)
            if (
                len(index) == 2
                and A[index[0]] == B[index[1]]
                and A[index[1]] == B[index[0]]
            ):
                return True
            if len(index) == 0 and len(A) - len(set(A)) > 0:
                return True
        return False


obj = Solution()
s = "ab"
goal = "ba"
print(obj.buddyStrings(s, goal))
