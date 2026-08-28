class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = {}
        double = 0
        for i in nums:
            if i not in seen:
                seen[i] = seen.get(i, 0) + 1
            else:
                double = i
        return double
            