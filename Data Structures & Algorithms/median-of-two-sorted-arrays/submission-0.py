class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        #iterate through nums1 and nums2
        #check which ones less than add to list (if equal add 1)
        # check length of array if divisible by 2 -> get mid  and add (mid + mid+1)/2 = median
        # if length is odd, get mid -> median
        
        inOrder = []
        i = 0
        j = 0
        n = max(len(nums1), len(nums2))
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                inOrder.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                inOrder.append(nums2[j])
                j += 1
            else:
                inOrder.append(nums1[i])
                inOrder.append(nums2[j])
                i += 1
                j += 1
        
        if i < len(nums1):
            for num in nums1[i:]:
                inOrder.append(num)
        if j < len(nums2): 
            for num in nums2[j:]:
                inOrder.append(num)
        
        length = len(inOrder)
        mid = length // 2
        if length % 2 == 0:
            median = (inOrder[mid] + inOrder[mid - 1]) / 2
        else:
            median = inOrder[mid]
        
        return median
            


    
