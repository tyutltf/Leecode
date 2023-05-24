# -*- encoding: utf-8 -*-
'''
@File    :   812-最大三角形面积.py
@Time    :   2023/05/24 11:35:05
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
from itertools import combinations
# here put the import lib
from typing import List

'''
给你一个由 X-Y 平面上的点组成的数组 points ，其中 points[i] = [xi, yi] 。从其中取任意三个不同的点组成三角形，返回能组成的最大三角形的面积。与真实值误差在 10-5 内的答案将会视为正确答案。

示例 1：

输入：points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
输出：2.00000
解释：输入中的 5 个点如上图所示，红色的三角形面积最大。
示例 2：

输入：points = [[1,0],[0,0],[0,1]]
输出：0.50000

提示：

3 <= points.length <= 50
-50 <= xi, yi <= 50
给出的所有点 互不相同
'''


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # a = combinations(points, 3)
        # for i in a:
        #     print(i)
        return max(abs(x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2) / 2 for (x1, y1), (x2, y2), (x3, y3) in combinations(points, 3))


obj = Solution()
points = [[0, 0],
          [0, 1],
          [1, 0],
          [0, 2],
          [2, 0]]
print(obj.largestTriangleArea(points))
