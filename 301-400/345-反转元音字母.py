''' 
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

 

示例 1：

输入："hello"
输出："holle"
示例 2：

输入："leetcode"
输出："leotcede"
 

提示：

元音字母不包含字母 "y" 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-vowels-of-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def reverseVowels(self, s: str):
        dic = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        l = 0
        r = len(s)-1
        s = list(s)
        print(s)
        while l < r:
            if s[l] in dic and s[r] in dic:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            if s[l] not in dic:
                l += 1
            if s[r] not in dic:
                r -= 1
        return ''.join(s)


obj = Solution()
print(obj.reverseVowels("leotcede"))
