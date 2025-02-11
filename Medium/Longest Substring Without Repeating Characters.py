class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        char_set = set()
        longest = 0
        
        for end in range(len(s)):
            # If the character at 'end' is in the set, move 'start' pointer to the right
            while s[end] in char_set:
                char_set.remove(s[start])
                start += 1
            
            # Add the current character to the set
            char_set.add(s[end])
            
            # Directly calculate the longest substring length during each iteration
            longest = max(longest, end - start + 1)
        
        return longest