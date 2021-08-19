# -*- encoding: utf-8 -*-
'''
@File    :   661-图片平滑器.py
@Time    :   2021/08/13 22:42:36
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
from typing import List
'''
包含整数的二维矩阵 M 表示一个图片的灰度。你需要设计一个平滑器来让每一个单元的灰度成为平均灰度 (向下舍入) ，平均灰度的计算是周围的8个单元和它本身的值求平均，如果周围的单元格不足八个，则尽可能多的利用它们。

示例 1:

输入:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
输出:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
解释:
对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0
对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0
对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0
注意:

给定矩阵中的整数范围为 [0, 255]。
矩阵的长和宽的范围均为 [1, 150]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/image-smoother
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def imageSmoother(self, M: List[List[int]]):
        # ans = [[0] * len(M[0]) for _ in M]
        # for row,col in [(i,j) for i in range(len(M)) for j in range(len(M[0]))]:
        #     count = 0
        #     for dx,dy in [(i,j) for i in range(row - 1,row + 2) for j in range(col - 1,col + 2)]:
        #         if 0 <= dx < len(M) and 0<= dy < len(M[0]):
        #             ans[row][col] += M[dx][dy]
        #             count += 1
        #     ans[row][col] //= count
        # return ans

        m = len(M[0])
        N = [[0.5]+i+[0.5] for i in M]
        N = [[0.5]*(m+2)] + N + [[0.5]*(m+2)]

        # 卷积
        for i in range(1, len(N)-1):
            for j in range(1, len(N[0])-1):
                total = [N[i-1][j-1], N[i][j-1], N[i+1][j-1], N[i-1][j],
                         N[i][j], N[i+1][j], N[i-1][j+1], N[i][j+1], N[i+1][j+1]]
                sums, k = 0, 0
                for _ in total:
                    if _ != 0.5:
                        sums += _
                    else:
                        k += 1
                M[i-1][j-1] = int(sums/(9-k))
        return M
