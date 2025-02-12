class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the smaller array for binary search efficiency
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        x, y = len(nums1), len(nums2)
        low, high = 0, x
        
        while low <= high:
            # Partition nums1 and nums2
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX
            
            # Edge cases handled by float('-inf') and float('inf')
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]
            
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]
            
            # Check if we have found the correct partitions
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # Found the correct partition
                if (x + y) % 2 == 0:
                    # Even total length
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                else:
                    # Odd total length
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                # Move partitionX to the left
                high = partitionX - 1
            else:
                # Move partitionX to the right
                low = partitionX + 1