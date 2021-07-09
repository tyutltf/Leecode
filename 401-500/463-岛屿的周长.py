# -*- encoding: utf-8 -*-
"""
@File    :   463-岛屿的周长.py
@Time    :   2021/07/06 22:27:42
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
"""
# here put the import lib
from typing import List

"""
给定一个 row x col 的二维网格地图 grid ，其中：grid[i][j] = 1 表示陆地， grid[i][j] = 0 表示水域。

网格中的格子 水平和垂直 方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。

岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。

示例 1：

输入：grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
输出：16
解释：它的周长是上面图片中的 16 个黄色的边
示例 2：

输入：grid = [[1]]
输出：4
示例 3：

输入：grid = [[1,0]]
输出：4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/island-perimeter
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


如果被计数的事物有 AA、BB、CC 三类，那么，AA 类和 BB 类和 CC 类元素个数总和 == AA 
类元素个数 ++ BB 类元素个数++ CC 类元素个数 —— 既是 AA 类又是 BB 类的元素个数 —— 既是 
AA 类又是 CC 类的元素个数 —— 既是 BB 类又是 CC 类的元素个数 ++ 既是 AA 类又是 BB 类而且是
 CC 类的元素个数。(A\cup B\cup C = A + B + C - A\cap B - B\cap C - C\cap A + A\cap B\cap C)(A∪B∪C=A+B+C−A∩B−B∩C−C∩A+A∩B∩C)

因此，在本题中，如果考虑仅有两个格子相交，假设一个叫做陆地 AA，另一个叫做陆地 BB，根据容斥原理，
它们各自的周长分别是 44，既属于 AA 又属于 BB 的边数是 22 条，所以 8 - 2 = 68−2=6。


再来看三个格子相交的情况，假设叫做陆地 AA，陆地 BB，陆地 CC，根据容斥原理，它们各自的周长分别是 44，
既属于 AA 又属于 BB 的有 22 条，既属于 AA 又属于 CC 的也有 22 条，BB 与 CC 不相交，那么总周长为 4*3 - 2*2 = 84∗3−2∗2=8


以此可以推广到更多的格子相交，因此，我们在遍历到每个点的时候，只需要对其下方或者右边判断是否有格子即可。

每个*4  -  重合部分*2

"""


class Solution:
    def islandPerimeter(self, grid: List[List[int]]):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    down = 2 if i < m - 1 and grid[i + 1][j] == 1 else 0
                    right = 2 if j < n - 1 and grid[i][j + 1] == 1 else 0
                    ans += 4 - down - right
        return ans


obj = Solution()
grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
print(obj.islandPerimeter(grid))
