# -*- encoding: utf-8 -*-
"""
@File    :   38-报数.py
@Time    :   2023/06/09 20:11:02
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
"""
"""
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。


"""


class Solution:
    def countAndSay(self, n: int) -> str:
        pre = ""
        cur = "1"

        # 从第 2 项开始
        for _ in range(1, n):
            # 这里注意要将 cur 赋值给 pre
            # 因为当前项，就是下一项的前一项。有点绕，尝试理解下
            pre = cur
            # 这里 cur 初始化为空，重新拼接
            cur = ""
            # 定义双指针 start，end
            start = 0
            end = 0
            # 开始遍历前一项，开始描述
            while end < len(pre):
                # 统计重复元素的次数，出现不同元素时，停止
                # 记录出现的次数，
                while end < len(pre) and pre[start] == pre[end]:
                    end += 1
                # 元素出现次数与元素进行拼接
                cur += str(end - start) + pre[start]
                # 这里更新 start，开始记录下一个元素
                start = end

        return cur
