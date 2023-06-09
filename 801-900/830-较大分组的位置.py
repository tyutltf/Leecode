# -*- encoding: utf-8 -*-
"""
@File    :   830-较大分组的位置.py
@Time    :   2023/06/09 20:43:13
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
"""
# here put the import lib
from typing import List

"""
在一个由小写字母构成的字符串 s 中，包含由一些连续的相同字符所构成的分组。

例如，在字符串 s = "abbxxxxzyy" 中，就含有 "a", "bb", "xxxx", "z" 和 "yy" 这样的一些分组。

分组可以用区间 [start, end] 表示，其中 start 和 end 分别表示该分组的起始和终止位置的下标。上例中的 "xxxx" 分组用区间表示为 [3,6] 。

我们称所有包含大于或等于三个连续字符的分组为 较大分组 。

找到每一个 较大分组 的区间，按起始位置下标递增顺序排序后，返回结果。

示例 1：

输入：s = "abbxxxxzzy"
输出：[[3,6]]
解释："xxxx" 是一个起始于 3 且终止于 6 的较大分组。
示例 2：

输入：s = "abc"
输出：[]
解释："a","b" 和 "c" 均不是符合要求的较大分组。
示例 3：

输入：s = "abcdddeeeeaabbbcd"
输出：[[3,5],[6,9],[12,14]]
解释：较大分组为 "ddd", "eeee" 和 "bbb"
示例 4：

输入：s = "aba"
输出：[]

提示：

1 <= s.length <= 1000
s 仅含小写英文字母
"""


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        temp = []
        for i in range(len(s)):
            if temp:
                if s[i] == temp[0]:
                    temp.append(s[i])
                else:
                    temp = [s[i]]
                # 获取长度>3的数据 并求下标
                if len(temp) >= 3:
                    _res = [i - len(temp) + 1, i]
                    if res and res[-1][0] == _res[0]:
                        res[-1] = _res
                    else:
                        res.append(_res)
            else:
                temp.append(s[i])
        return res


s = "abcdddeeeeaabbbcd"
s = "aaa"
obj = Solution()
print(obj.largeGroupPositions(s))
