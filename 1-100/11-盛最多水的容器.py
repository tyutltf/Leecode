'''
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。



图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。



示例:

输入: [1,8,6,2,5,4,8,3,7]
输出: 49
'''
maxarea=0
li=[1,8,6,2,5,4,8,3,7]
for i in range(len(li)):
    #print(li[i])
    for j in range(i,len(li)):
        #print(li[j])
        area=(j-i)*min(li[i],li[j])
        if area >maxarea:
            maxarea=area
print(maxarea)

height=[1,8,6,2,5,4,8,3,7]
head, tail = 0, len(height) - 1  #头指针为0，尾指针为长度减一即8
maxarea1 = 0
while head < tail:
    area_height = min(height[head], height[tail])
    area_width = tail - head
    volume = area_height * area_width
    if volume > maxarea1:
        maxarea1 = volume
    if height[head] < height[tail]:
        head += 1
    else:
        tail -= 1
print(maxarea1)

