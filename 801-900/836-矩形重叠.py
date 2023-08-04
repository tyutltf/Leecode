# -*- encoding: utf-8 -*-
"""
@File    :   836-矩形重叠.py
@Time    :   2023/08/03 09:48:05
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
"""
# here put the import lib
from typing import List

"""
矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。矩形的上下边平行于 x 轴，左右边平行于 y 轴。

如果相交的面积为 正 ，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。

给出两个矩形 rec1 和 rec2 。如果它们重叠，返回 true；否则，返回 false 。


示例 1：

输入：rec1 = [0,0,2,2], rec2 = [1,1,3,3]
输出：true
示例 2：

输入：rec1 = [0,0,1,1], rec2 = [1,0,2,1]
输出：false
示例 3：

输入：rec1 = [0,0,1,1], rec2 = [2,2,3,3]
输出：false


提示：

rect1.length == 4
rect2.length == 4
-109 <= rec1[i], rec2[i] <= 109
rec1 和 rec2 表示一个面积不为零的有效矩形
"""

"""
乍一看，要考虑的情况似乎很多，两矩形到底是怎么一个重叠情况也不清楚，一不小心就少考虑了一种。

事实上题目中的坐标系提醒了我，我们只要将这题中的两个矩形看成是两个可行域，求这两个可行域的交集，也就是最终的可行域即可。

最终只要判断最终的可行域面积是否大于0即可

"""


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1 = max(rec1[0], rec2[0])
        y1 = max(rec1[1], rec2[1])

        x2 = min(rec1[2], rec2[2])
        y2 = min(rec1[3], rec2[3])

        if x1 < x2 and y1 < y2:
            return True
        else:
            return False


obj = Solution()
rec1 = [0, 0, 1, 1]
rec2 = [2, 2, 3, 3]

print(obj.isRectangleOverlap(rec1, rec2))
