class Solution(object):
    def plusOne(self, digits):
        num = 0
        for i in range(len(digits)):
            num += digits[i] * (10 ** (len(digits) - 1 - i))  # accumulate
        num += 1
        return [int(d) for d in str(num)]