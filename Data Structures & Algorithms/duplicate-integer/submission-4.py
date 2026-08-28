class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        org_val = set()
        for val in nums:
            if val not in org_val:
                org_val.add(val)
            else:
                return True
        return False

            
        