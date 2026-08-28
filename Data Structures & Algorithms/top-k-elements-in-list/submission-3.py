class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #use dictionary to track amount of numbers present in list
        #use k value as end of for loop pulling largest values in dictionary first appenfing them to a list
        ans = []
        total = {}
        for n in nums:
            # add each number to set and update value
            if n not in total:
                total[n] = 0
            total[n] += 1
        sorted_items = sorted(total.items(),key=lambda item:item[1], reverse=True)
        for i in range(k):
            ans.append(sorted_items[i][0])
        
        return ans



