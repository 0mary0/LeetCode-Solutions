class Solution(object):
    def strStr(self, haystack, needle):
        for j in range(len(haystack) - len(needle) + 1):
            temp = 0
            while temp < len(needle) and haystack[j + temp] == needle[temp]:
                temp += 1
            if temp == len(needle):
                return j
        return -1