'''
给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。
示例 2:

输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.
说明: 你算法的时间复杂度应为 O(log n) 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/factorial-trailing-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def trailingZeroes(self, num: int) -> int:
        factorial = 1
        # 求阶乘
        for i in range(1, num + 1):
            factorial = factorial*i
        # 求出尾数有几个零
        data = '.'.join(str(factorial))
        res = data.split('.')
        res.reverse()
        num = 0
        for i in res:
            if i == '0':
                num += 1
            else:
                return num
        return num

    def trailingZeroes_good(self, n: int) -> int:
        num = 0
        while n > 0:
            num += n // 5
            n = n // 5
        return num


obj = Solution()
print(obj.trailingZeroes(5))
