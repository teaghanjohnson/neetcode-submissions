class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1
        res = -1

        if target not in nums:
            return res

        while l <= r:
            mid = (l + r) // 2
            if nums[l] == target:
                return l

            if nums[mid] == target:
                return mid
            if nums[r] == target:
                return r
              
            l += 1
            r -= 1


        
    
                

