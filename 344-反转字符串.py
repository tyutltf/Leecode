''' 

编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。

 

示例 1：

输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]
示例 2：

输入：["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]
'''

class Solution:
    def reverseString(self, s):
        # 普通解法
        # count=len(s)
        # for i in range(count//2):
        #     s[i],s[count-1-i]=s[count-1-i],s[i]
        # return s

        # 定义指针
        left = 0
        right = len(s) - 1
        # left、right 指针重合前，遍历数组，交换字符
        while left < right:
            # 交换字符
            s[left], s[right] = s[right], s[left]
            # 移动指针
            left += 1
            right -= 1
        return s

obj=Solution()
print(obj.reverseString(["H","a","n","n","a","h"]))