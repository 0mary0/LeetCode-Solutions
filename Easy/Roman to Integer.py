class Solution(object):
    def romanToInt(self, s):
        answer = 0
        RomanNum = { "I": 1, "V": 5, "X":10, "L": 50, "C": 100, "D": 500, "M": 1000}
        prev = 0
        for char in reversed(s):
            value = RomanNum[char]

            if value < prev :
                answer -= value
            
            else:
                answer += value
            
            prev = value
        
        return answer