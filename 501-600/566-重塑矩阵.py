# -*- encoding: utf-8 -*-
'''
@File    :   566-重塑矩阵.py
@Time    :   2021/08/09 20:13:54
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
from typing import List
'''
在 MATLAB 中，有一个非常有用的函数 reshape ，它可以将一个 m x n 矩阵重塑为另一个大小不同（r x c）的新矩阵，但保留其原始数据。

给你一个由二维数组 mat 表示的 m x n 矩阵，以及两个正整数 r 和 c ，分别表示想要的重构的矩阵的行数和列数。

重构后的矩阵需要将原始矩阵的所有元素以相同的 行遍历顺序 填充。

如果具有给定参数的 reshape 操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。

示例 1：


输入：mat = [[1,2],[3,4]], r = 1, c = 4
输出：[[1,2,3,4]]
示例 2：


输入：mat = [[1,2],[3,4]], r = 2, c = 4
输出：[[1,2],[3,4]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reshape-the-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int):
        # 如果 r*c 不等于 数量则不能重塑
        nums = len(mat[0])*len(mat)
        if r*c != nums:
            return mat
        one = [i for arr in mat for i in arr]
        # 循环构建矩阵
        res = []
        for i in range(0, nums, c):
            temp = one[i:i+c]
            res.append(temp)
        return res

        # 官方解法 前半部分一致 后半部分没有看明白
        # m, n = len(mat), len(mat[0])
        # if m * n != r * c:
        #     return mat

        # ans = [[0] * c for _ in range(r)]
        # for x in range(m * n):
        #     ans[x // c][x % c] = mat[x // n][x % n]

        # return ans


obj = Solution()
mat = [[1, 2, 3, 4]]
r = 4
c = 1
print(obj.matrixReshape(mat, r, c))
