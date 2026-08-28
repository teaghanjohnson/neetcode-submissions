class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        org_val = []
        for val in nums:
            if val not in org_val:
                org_val.append(val)
            else:
                return True
        return False

            
        