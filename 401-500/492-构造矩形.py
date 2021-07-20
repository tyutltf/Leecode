# -*- encoding: utf-8 -*-
'''
@File    :   492-构造矩形.py
@Time    :   2021/07/20 21:34:45
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
import math
'''
作为一位web开发者， 懂得怎样去规划一个页面的尺寸是很重要的。 现给定一个具体的矩形页面面积，你的任务是设计一个长度为 L 和宽度为 W 且满足以下要求的矩形的页面。要求：

1. 你设计的矩形页面必须等于给定的目标面积。

2. 宽度 W 不应大于长度 L，换言之，要求 L >= W 。

3. 长度 L 和宽度 W 之间的差距应当尽可能小。
你需要按顺序输出你设计的页面的长度 L 和宽度 W。

示例：

输入: 4
输出: [2, 2]
解释: 目标面积是 4， 所有可能的构造方案有 [1,4], [2,2], [4,1]。
但是根据要求2，[1,4] 不符合要求; 根据要求3，[2,2] 比 [4,1] 更能符合要求. 所以输出长度 L 为 2， 宽度 W 为 2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-the-rectangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 解题思路
# 对这个数开方，然后往下递减，遇到第一个可以整除的，就是最好的结果，且为宽度
# 为什么要开方：题中要求找到L,W最相近的结果，那么最理想的情况是这个数可以开方，L=W，当他不能开方的时候，找到最接近平方根的数应该就是结果


class Solution:
    def constructRectangle(self, area: int):
        W = int(math.sqrt(area))
        while area % W != 0:
            W -= 1
        return [int(area/W), W]


obj = Solution()
print(obj.constructRectangle(14))
