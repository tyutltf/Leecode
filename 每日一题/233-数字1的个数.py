# -*- encoding: utf-8 -*-
'''
@File    :   233-数字1的个数.py
@Time    :   2021/08/13 19:20:59
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
'''
给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。

示例 1：

输入：n = 13
输出：6
示例 2：

输入：n = 0
输出：0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-digit-one
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def countDigitOne(self, n: int):
        # # 暴力解法 超时了
        # res = 0
        # for i in range(1, n+1):
        #     temp = str(i).count('1')
        #     res += temp
        # return res

        # 思路 分别计算各个位置上1出现的次数 最后求和
        if n <= 0:
            return 0
        res = 0
        # base用来表示当前是计算哪个位置，比如说base等于1就表示是计算个位数，base=10表示当前计算十位数
        base = 1
        while n // base != 0:
            # cur_num表示当前位置上的数字
            cur_num = (n // base) % 10
            # high_num表示高位的数字，比如说当前计算十位数出现1的个数，那么1812中high_pos就应该是18
            high_num = n // (base * 10)
            # low_num表示低位的数字，比如说上面的例子就是2
            low_num = n - (n // base) * base
            # 接下来就是比较当前数字和1的大小
            # 1.如果=0，那么当前位置出现1的个数只取决于高位
            # 2.如果=1，那么当前位置出现1的个数不光取决于高位，还取决于低位
            # 3.如果>1,那么当前位置出现1的个数只取决于高位
            if cur_num == 0:
                res += high_num * base
            elif cur_num == 1:
                res += (high_num * base + (low_num + 1))
            else:
                res += (high_num + 1) * base
            # 计算下一个位置的1的个数，base需要*10
            base *= 10
        return res


n = 13
obj = Solution()
print(obj.countDigitOne(n))
