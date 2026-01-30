class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        first = strs[0]
        i = 0

        while i < len(first):
            for s in strs:
                if i >= len(s) or s[i] != first[i]:
                    return first[:i]
            i += 1

        return first
