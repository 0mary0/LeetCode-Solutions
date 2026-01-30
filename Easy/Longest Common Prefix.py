class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        i = 0
        while True:
            for s in strs:
                if i >= len(s) or s[i] != strs[0][i]:
                    return strs[0][:i]
            i += 1
