# -*- encoding: utf-8 -*-
'''
@File    :   504-七进制数.py
@Time    :   2021/07/21 21:46:04
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
'''
给定一个整数，将其转化为7进制，并以字符串形式输出。

示例 1:

输入: 100
输出: "202"
示例 2:

输入: -7
输出: "-10"
注意: 输入范围是 [-1e7, 1e7] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/base-7
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

算法设计：依次计算num与7的商作为七进制的一位，存储到列表中，num整除7进行更新，
直到小于7退出循环。根据短除法可知，此处少了最后的商，两种解决思路：一是改变循环条件，
再除一次，此时的余数添加成功，且商一定会变为0，退出循环；二是在循环结束添加商。
同时用列表存储的七进制数与真实的七进制数方向正好相反，进行一次简单的调整方向即可。

'''


class Solution:
    def convertToBase7(self, num: int):
        base7 = []
        if num < 0:
            flag = 1
            num = -num
        else:
            flag = 0
        while num >= 7:
            fig = str(num % 7)
            base7.append(fig)
            num = num // 7
        base7.append(str(num))
        if flag:
            base7.append('-')
        base7.reverse()
        return ''.join(base7)


object = Solution()
print(object.convertToBase7(100))
