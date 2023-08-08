# -*- encoding: utf-8 -*-
"""
@File    :   867-转置矩阵.py
@Time    :   2023/08/04 15:49:55
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
"""
# here put the import lib
from typing import List

"""
给你一个二维整数数组 matrix， 返回 matrix 的 转置矩阵 。

矩阵的 转置 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。


示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[1,4,7],[2,5,8],[3,6,9]]
示例 2：

输入：matrix = [[1,2,3],[4,5,6]]
输出：[[1,4],[2,5],[3,6]]


提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
-109 <= matrix[i][j] <= 109
"""

"""
解题思路
理解了zip函数的原理，很容易想到用它来做转置操作： zip(iter1,iter2,...)函数将可迭代的对象作为参数，
将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。例如：

a = [1,2,3]
b = [4,5,6]
zip(a,b)   # 输出 [(1, 4), (2, 5), (3, 6)]
看吧，如果把a和b看成一个矩阵的两行，那zip(a,b)就输出了这个矩阵转置的结果。

那么在我们这题里怎么用呢？

题目里的matrix的数据类型是List[List[int]]（m == matrix.length n == matrix[i].length），

如果我们把第二层的m个list输入zip函数就能得到最终结果。

再补充一个python3里可变参数*arg的用法，该方法允许我们把list或者tuple里的元素作为可变参数传入代码

"""


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # row, col = len(matrix), len(matrix[0])
        # res = []
        # for i in range(col):
        #     temp = []
        #     for j in range(row):
        #         temp.append(matrix[j][i])
        #     res.append(temp)
        # return res

        # row, col = len(matrix), len(matrix[0])
        # res = [[0] * row for i in range(col)]
        # for i in range(row):
        #     for j in range(col):
        #         res[j][i] = matrix[i][j]
        # return res

        return list(zip(*matrix))


obj = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[1, 2, 3], [4, 5, 6]]
print(obj.transpose(matrix))
