# -*- encoding: utf-8 -*-
"""
@File    :   860-柠檬水找零.py
@Time    :   2023/08/04 14:44:26
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
"""
# here put the import lib
from typing import List

"""
在柠檬水摊上，每一杯柠檬水的售价为 5 美元。顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。

每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。

注意，一开始你手头没有任何零钱。

给你一个整数数组 bills ，其中 bills[i] 是第 i 位顾客付的账。如果你能给每位顾客正确找零，返回 true ，否则返回 false 。



示例 1：

输入：bills = [5,5,5,10,20]
输出：true
解释：
前 3 位顾客那里，我们按顺序收取 3 张 5 美元的钞票。
第 4 位顾客那里，我们收取一张 10 美元的钞票，并返还 5 美元。
第 5 位顾客那里，我们找还一张 10 美元的钞票和一张 5 美元的钞票。
由于所有客户都得到了正确的找零，所以我们输出 true。
示例 2：

输入：bills = [5,5,10,10,20]
输出：false
解释：
前 2 位顾客那里，我们按顺序收取 2 张 5 美元的钞票。
对于接下来的 2 位顾客，我们收取一张 10 美元的钞票，然后返还 5 美元。
对于最后一位顾客，我们无法退回 15 美元，因为我们现在只有两张 10 美元的钞票。
由于不是每位顾客都得到了正确的找零，所以答案是 false。


提示：

1 <= bills.length <= 105
bills[i] 不是 5 就是 10 或是 20
"""

"""
题解
由于 101010 美元钞票只能用于 202020 美元的找零，而 555 美元钞票既可以用于 202020 美元的找零，又可以用于 101010 美元的找零，更加通用（使用场景更多），所以如果可以用 101010 美元，应当优先用 101010 美元，其次用 555 美元。如果优先用 555 美元，可能会面临 bills[i]=10\textit{bills}[i]=10bills[i]=10 无法找零的情况。

设当前有 five\textit{five}five 张 555 美元钞票，ten\textit{ten}ten 张 101010 美元钞票。202020 美元的无需统计，因为它无法用来找零。

设 b=bills[i]b=\textit{bills}[i]b=bills[i]，分类讨论：

如果 b=5b=5b=5，无需找零，five\textit{five}five 加一。
如果 b=10b=10b=10，返还 555 美元，five\textit{five}five 减一，ten\textit{ten}ten 加一。
如果 b=20b=20b=20 且 ten>0\textit{ten}>0ten>0，返还 10+510+510+5 美元，five\textit{five}five 和 ten\textit{ten}ten 都减一。
如果 b=20b=20b=20 且 ten=0\textit{ten}=0ten=0，返还 5+5+55+5+55+5+5 美元，five\textit{five}five 减三。
如果发现 five<0\textit{five}<0five<0，说明无法正确找零，返回 false。
如果中途没有返回 false，那么循环结束后返回 true。

"""


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for b in bills:
            if b == 5:  # 无需找零
                five += 1
            elif b == 10:  # 返还 5
                five -= 1
                ten += 1
            elif ten:  # 此时 b=20，返还 10+5
                five -= 1
                ten -= 1
            else:  # 此时 b=20，返还 5+5+5
                five -= 3
            if five < 0:  # 无法正确找零
                return False
        return True


obj = Solution()
bills = [5, 5, 5, 10, 20]
print(obj.lemonadeChange(bills))
