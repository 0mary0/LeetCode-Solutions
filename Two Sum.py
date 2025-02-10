class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {} # Create an empty hashmap to store the numbers we have seen so far and their indices
        for i,num in enumerate(nums): # Go through the list of numbers
            complement = target - num 
            
            if complement in hashmap: # If the number is in the hashmap, it's the answer
                return [hashmap[complement], i]
            
            hashmap [num] = i

        return []
