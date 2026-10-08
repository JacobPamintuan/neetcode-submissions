class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        
        buckets = [[] for _ in range(len(nums)+1)]

        for num, count in freq.items():
            buckets[count].append(num)

        ans = []
        
        for bucket in reversed(buckets):
            
            for num in bucket:
                if k == 0: 
                    return ans
                ans.append(num)
                k -= 1

            if k == 0:
                return ans
            
            
