class Solution(object):
    def isPalindrome(self, x):
        if x<0 or (x%10==0 and x!=0):
            return False
        
        revnum = 0 #Initialize reversed number

        while x>revnum: #Store reversed x in revnum
            revnum = revnum*10 + x%10
            x = x//10

        return x==revnum or x==revnum // 10 #Compare x and it's reversed version, for both even and odd numbers