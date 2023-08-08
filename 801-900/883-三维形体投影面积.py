# -*- encoding: utf-8 -*-
"""
@File    :   883-三维形体投影面积.py
@Time    :   2023/08/08 11:18:10
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
"""
# here put the import lib
from typing import List

"""
在 n x n 的网格 grid 中，我们放置了一些与 x，y，z 三轴对齐的 1 x 1 x 1 立方体。

每个值 v = grid[i][j] 表示 v 个正方体叠放在单元格 (i, j) 上。

现在，我们查看这些立方体在 xy 、yz 和 zx 平面上的投影。

投影 就像影子，将 三维 形体映射到一个 二维 平面上。从顶部、前面和侧面看立方体时，我们会看到“影子”。

返回 所有三个投影的总面积 。

示例 1：

输入：[[1,2],[3,4]]
输出：17
解释：这里有该形体在三个轴对齐平面上的三个投影(“阴影部分”)。
示例 2:

输入：grid = [[2]]
输出：5
示例 3：

输入：[[1,0],[0,2]]
输出：8

提示：

n == grid.length == grid[i].length
1 <= n <= 50
0 <= grid[i][j] <= 50

终于读懂题意了：数组是一排排码放的;

第一排就是数组grid[0] = [1,2] ==> 表示两个箱子高度分别是 1、2 ；

第二排就是数组grid[1] = [3,4] ==> 表示两个箱子高度分别是 3、4；

最后就是分别映射三个平面了。

"""


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        x = sum([max(row) for row in grid])
        y = sum([max([grid[i][j] for i in range(n)]) for j in range(n)])
        z = sum(
            [sum([1 if grid[i][j] != 0 else 0 for i in range(n)]) for j in range(n)]
        )
        return x + y + z


obj = Solution()
grid = [[1, 2], [3, 4]]
print(obj.projectionArea(grid))
