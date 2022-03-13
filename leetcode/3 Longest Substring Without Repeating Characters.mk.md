
# 3. Longest Substring Without Repeating Characters
最长无重复字符字串 
<br>
# 题目内容
Given a string s, find the length of the longest substring without repeating characters.
给定一个字符串，找到其中没有重复字符的最长子串。
<br>
###example
![image.png](https://upload-images.jianshu.io/upload_images/10481414-95a1d592f7a5244f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

# 题目思考
我看到题目一开始想的是，可以通过两个循环进行嵌套。
第一个循环遍历字符串内的所有字符，定义为left位。
第二个循环控制一个下标，让下标从第一个循环的left位开始，找一个right位。并通过index方法，为left和right范围内的字符进行判断是否有重复的字符。判断每个字符的下一个index是否在left-right的范围内。
这样感觉实现起来比较复杂。就不做过多赘述。
# 答案解析
方法一：暴力破解法
```
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def check(start, end):
            chars = [0] * 128
            for i in range(start, end + 1):
                c = s[i]
                chars[ord(c)] += 1
                if chars[ord(c)] > 1:
                    return False
            return True

        n = len(s)

        res = 0
        for i in range(n):
            for j in range(i, n):
                if check(i, j):
                    res = max(res, j - i + 1)
        return res
```
暴力破解就会比较简单，从左至右依次循环。用所有的left 和 right进行排列组合。每一个排列组合判断其中是否有重复的字符。如果没有，则比较并记录最大长度值。
由于相当于是内外嵌套了三个循环，所以时间复杂度可以看作n^3。
<br>
方法二
```
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0] * 128

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1

            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1

            res = max(res, right - left + 1)

            right += 1
        return res
```
方法二是采用滑动窗口的形式。left和right分别控制左右两个边界。
***我一直觉得利用一个128的数组来控制是否有重复的字符，是一个比较好的方法***
先第一个循环遍历字符串内所有字符。
当遇到重复字符的时候，从left到right遍历滑动窗口。将left遍历到重复字符所在的位置后一位，将left之前的字符置空。这意味着这时候包含right在内，从left到right 又没有重复字符了。
接着继续重复操作，比较并记录最大值。
这里的时间复杂度可以看作只有2n，因为并不属于嵌套循环，left和right的下标最大也只会遍历一遍字符串。

>此内容只用做本人知识巩固，别无他用。