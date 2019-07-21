"""
给定一个字符串，找出不含重复字符串的最长子串的长度。
例如：输入“abcabcbb”
输出：3
解释：无重复字符串的最大子串为abc，长度为3
"""
#!/usr/bin/python
# _*_ coding: utf-8 _*_


class Solution:
    def lengthOflongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        temp = 0
        d = {}
        start = 0
        for i in range(len(s)):
            if s[i] in d and start <= d[s[i]]:
                start = d[s[i]] + 1
            temp = max(i-start+1, temp)
            d[s[i]] = i
        return temp

    print(lengthOflongestSubstring('abcabcbb'))
