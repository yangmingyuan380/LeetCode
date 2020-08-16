# -*- coding: utf-8 -*-
"""
--------------------------
    @Author : 杨向文
    @file : 14最长公共前缀.py
    @time : 2020/8/16 16:19
--------------------------
"""


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        qianzhui = ''
        if len(strs):
            s = strs[0]
            for i in range(len(s)):
                for ss in strs[1:]:
                    if s[:i+1] == ss[:i+1]:
                        pass
                    else:
                        return qianzhui
                qianzhui = s[0:i+1]
        return qianzhui


if __name__ == "__main__":
    sol = Solution()
    s = ["flower", "flow", "flight"]
    print(sol.longestCommonPrefix(s))
    s1 = ["dog","racecar","car"]
    print(sol.longestCommonPrefix(s1))
