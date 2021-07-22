# -*- encoding: utf-8 -*-
'''
@File    :   509-斐波那契数列.py
@Time    :   2021/07/22 22:40:10
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
'''
斐波那契数，通常用 F(n) 表示，形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0，F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
给你 n ，请计算 F(n) 。

示例 1：

输入：2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fibonacci-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def fib(self, n: int):
        # * 递推，动态规划，优化存储 只用记录前两个结果即可，改为使用两个变量交替
        # a, b = 0, 1
        # for i in range(n):
        #     a, b = b, a + b
        # return a

        # * 直接递归 fib(n) = fib(n-1) + fib(n-2)
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)


obj = Solution()
print(obj.fib(4))
