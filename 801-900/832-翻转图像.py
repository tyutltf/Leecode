# -*- encoding: utf-8 -*-
"""
@File    :   832-翻转图像.py
@Time    :   2023/06/09 20:36:22
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
"""
# here put the import lib
from typing import List

"""
给定一个 n x n 的二进制矩阵 image ，先 水平 翻转图像，然后 反转 图像并返回 结果 。

水平翻转图片就是将图片的每一行都进行翻转，即逆序。

例如，水平翻转 [1,1,0] 的结果是 [0,1,1]。
反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。

例如，反转 [0,1,1] 的结果是 [1,0,0]。


示例 1：

输入：image = [[1,1,0],[1,0,1],[0,0,0]]
输出：[[1,0,0],[0,1,0],[1,1,1]]
解释：首先翻转每一行: [[0,1,1],[1,0,1],[0,0,0]]；
     然后反转图片: [[1,0,0],[0,1,0],[1,1,1]]
示例 2：

输入：image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
输出：[[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
解释：首先翻转每一行: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]；
     然后反转图片: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
"""


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # 解法1 按部就班
        # res = []
        # for i in image:
        #     # 翻转
        #     r_i = i[::-1]
        #     # 求1-每个数的绝对值
        #     abs_i = [1-j for j in r_i]
        #     res.append(abs_i)
        # return res
        # 解法2 双指针
        for i in image:
            _l, _r = 0, len(i) - 1
            while _l <= _r:
                print(_l, _r)
                if _l != _r:
                    if i[_l] == i[_r]:
                        i[_l] = 1 - i[_l]
                        i[_r] = 1 - i[_r]
                else:
                    i[_l] = abs(1 - i[_l])
                _l += 1
                _r -= 1
        return image


obj = Solution()
# image = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
print(obj.flipAndInvertImage(image))
