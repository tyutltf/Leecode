# -*- encoding: utf-8 -*-
'''
@File    :   804-唯一摩尔斯密码.py
@Time    :   2022/08/30 14:19:01
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
from typing import List

'''
国际摩尔斯密码定义一种标准编码方式，将每个字母对应于一个由一系列点和短线组成的字符串， 比如:

'a' 对应 ".-" ，
'b' 对应 "-..." ，
'c' 对应 "-.-." ，以此类推。
为了方便，所有 26 个英文字母的摩尔斯密码表如下：

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
给你一个字符串数组 words ，每个单词可以写成每个字母对应摩尔斯密码的组合。

例如，"cab" 可以写成 "-.-..--..." ，(即 "-.-." + ".-" + "-..." 字符串的结合)。我们将这样一个连接过程称作 单词翻译 。
对 words 中所有单词进行单词翻译，返回不同 单词翻译 的数量。

示例 1：

输入: words = ["gin", "zen", "gig", "msg"]
输出: 2
解释: 
各单词翻译如下:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

共有 2 种不同翻译, "--...-." 和 "--...--.".
示例 2：

输入：words = ["a"]
输出：1

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/unique-morse-code-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # words = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        # chars = [chr(i) for i in range(97, 97+26)]
        # chr_dict = dict(zip(chars,words))
        chr_dict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}
        print(chr_dict)
        # 可以用列表推导式
        # translate_words = []
        # for word in words:
        #     temp = [chr_dict.get(i) for i in list(word)]
        #     temp_str = ''.join(temp)
        #     translate_words.append(temp_str)
        translate_words = [''.join([chr_dict.get(i) for i in word]) for word in words]
        print(translate_words)
        count = len(set(translate_words))
        return count
        
            

obj = Solution()
words = ['awe','b','c','d','e','f','g','g']
print(obj.uniqueMorseRepresentations(words))