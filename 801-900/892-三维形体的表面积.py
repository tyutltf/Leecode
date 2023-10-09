# -*- encoding: utf-8 -*-
"""
@File    :   892-三维形体的表面积.py
@Time    :   2023/10/09 20:34:55
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
"""
# here put the import lib
from typing import List

"""
给你一个 n * n 的网格 grid ，上面放置着一些 1 x 1 x 1 的正方体。每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。

放置好正方体后，任何直接相邻的正方体都会互相粘在一起，形成一些不规则的三维形体。

请你返回最终这些形体的总表面积。

注意：每个形体的底面也需要计入表面积中。


示例 1：


输入：grid = [[1,2],[3,4]]
输出：34
示例 2：


输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
输出：32
示例 3：


输入：grid = [[2,2,2],[2,1,2],[2,2,2]]
输出：46


提示：

n == grid.length
n == grid[i].length
1 <= n <= 50
0 <= grid[i][j] <= 50
"""


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        a = 0
        # 计算大于0的个数 计算上下底面积
        ans = 0
        # 计算侧面积
        n = len(grid)
        for i in range(n):
            row = 0
            lie = 0
            for j in range(n):
                if grid[i][j] > 0:
                    a = a + 1
                ans = ans + abs(row - grid[i][j]) + abs(lie - grid[j][i])
                lie = grid[j][i]
                row = grid[i][j]
            ans = ans + row + lie
        return ans + a * 2


grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
obj = Solution()
print(obj.surfaceArea(grid))
