# -*- encoding: utf-8 -*-
'''
@File    :   717-1比特与2比特字符.py
@Time    :   2021/12/02 20:02:40
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
from typing import List
'''
有两种特殊字符。第一种字符可以用一比特0来表示。第二种字符可以用两比特(10 或 11)来表示。

现给一个由若干比特组成的字符串。问最后一个字符是否必定为一个一比特字符。给定的字符串总是由0结束。

示例 1:

输入:
bits = [1, 0, 0]
输出: True
解释:
唯一的编码方式是一个两比特字符和一个一比特字符。所以最后一个字符是一比特字符。
示例 2:

输入:
bits = [1, 1, 1, 0]
输出: False
解释:
唯一的编码方式是两比特字符和两比特字符。所以最后一个字符不是一比特字符。
注意:

1 <= len(bits) <= 1000.
bits[i] 总是0 或 1.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/1-bit-and-2-bit-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def isOneBitCharacter(self, bits: List[int]):
        # * 遍历bits 1的时候走两步 0的时候走一步
        # n = len(bits) - 1
        # i = 0
        # while i < n:
        #     if bits[i] == 1:
        #         i += 2
        #     else:
        #         i += 1
        # return i == n

        for inx, i in enumerate(bits):
            print(inx, i)
            if i:
                bits[inx] = bits[inx+1] = None
        return bits[-1] == 0


obj = Solution()
bits = [1, 1, 1, 0]
print(obj.isOneBitCharacter(bits))
