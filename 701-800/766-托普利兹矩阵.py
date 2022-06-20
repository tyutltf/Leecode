'''
给你一个 m x n 的矩阵 matrix 。如果这个矩阵是托普利茨矩阵，返回 true ；否则，返回 false 。

如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是 托普利茨矩阵 。

示例 1：

输入：matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
输出：true
解释：
在上述矩阵中, 其对角线为: 
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]"。
各条对角线上的所有元素均相同, 因此答案是 True 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/toeplitz-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # 后一行去除第一个元素等于前一行去除最后一个元素即可
        row = len(matrix)
        col = len(matrix[0])
        if row == 1 or col == 1:
            return True
        for i in range(row-1):
            front_data = matrix[i][:-1]
            behind_data = matrix[i+1][1::]
            if front_data != behind_data:
                return False
        return True


obj = Solution()
matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
obj.isToeplitzMatrix(matrix)
