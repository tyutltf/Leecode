# -*- encoding: utf-8 -*-
'''
@File    :   1154-一年中的第几天.py
@Time    :   2021/12/21 19:59:48
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
# import datetime

from itertools import accumulate

'''
给你一个字符串 date ，按 YYYY-MM-DD 格式表示一个 现行公元纪年法 日期。请你计算并返回该日期是当年的第几天。

通常情况下，我们认为 1 月 1 日是每年的第 1 天，1 月 2 日是每年的第 2 天，依此类推。每个月的天数与现行公元纪年法（格里高利历）一致。

 

示例 1：

输入：date = "2019-01-09"
输出：9
示例 2：

输入：date = "2019-02-10"
输出：41
示例 3：

输入：date = "2003-03-01"
输出：60
示例 4：

输入：date = "2004-03-01"
输出：61
 

提示：

date.length == 10
date[4] == date[7] == '-'，其他的 date[i] 都是数字
date 表示的范围从 1900 年 1 月 1 日至 2019 年 12 月 31 日

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/day-of-the-year
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def dayOfYear(self, date: str) -> int:
        # date_split = date.split('-')
        # start = date_split[0]+'-01-01'
        # diff = datetime.datetime.strptime(
        #     date, "%Y-%m-%d")-datetime.datetime.strptime(start, "%Y-%m-%d")
        # return diff.days+1

        # 第二种解法 判断闰年 accumulate函数是计算列表前缀和
        days = [0] + list(accumulate([31, 28, 31, 30, 31,
                                      30, 31, 31, 30, 31, 30, 31]))
        y, m, d = int(date[:4]), int(date[5:7]), int(date[-2:])
        if m > 2 and (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)):
            return days[m - 1] + d + 1
        return days[m - 1] + d


obj = Solution()
date = '2019-02-10'
print(obj.dayOfYear(date))
