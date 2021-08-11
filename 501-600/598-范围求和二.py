# -*- encoding: utf-8 -*-
'''
@File    :   598-范围求和二.py
@Time    :   2021/08/11 20:03:09
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
from typing import List
'''
给定一个初始元素全部为 0，大小为 m*n 的矩阵 M 以及在 M 上的一系列更新操作。

操作用二维数组表示，其中的每个操作用一个含有两个正整数 a 和 b 的数组表示，含义是将所有符合 0 <= i < a 以及 0 <= j < b 的元素 M[i][j] 的值都增加 1。

在执行给定的一系列操作后，你需要返回矩阵中含有最大整数的元素个数。

示例 1:

输入:
m = 3, n = 3
operations = [[2,2],[3,3]]
输出: 4
解释:
初始状态, M =
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]

执行完操作 [2,2] 后, M =
[[1, 1, 0],
 [1, 1, 0],
 [0, 0, 0]]

执行完操作 [3,3] 后, M =
[[2, 2, 1],
 [2, 2, 1],
 [1, 1, 1]]

M 中最大的整数是 2, 而且 M 中有4个值为2的元素。因此返回 4。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-addition-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def maxCount(self, m: int, n: int, operations: List[List[int]]):
        # # 暴力法 超时了。。。
        # juzhen = [[0]*m for i in range(n)]
        # for i in operations:
        #     temp = []
        #     for j in range(i[0]):
        #         for k in range(i[1]):
        #             temp.append([j, k])
        #     for i in temp:
        #         juzhen[i[0]][i[1]] += 1
        # # 接下来就是求二维列表最大元素个数
        # juzhen = [n for a in juzhen for n in a]
        # max_num = max(juzhen)
        # res = 0
        # for i in juzhen:
        #     if i == max_num:
        #         res += 1
        # return res

        # 求重叠面积的方法
        if not operations:
            return m*n
        i, j = operations[0][0], operations[0][1]
        for u, v in operations:
            i = min(i, u)
            j = min(j, v)
        return i*j


obj = Solution()
m, n = 3, 3
operations = [[2, 2], [3, 3]]
print(obj.maxCount(m, n, operations))
