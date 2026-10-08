class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        seen = set()

        for num in nums:
            seen.add(num)

        longest = 1
        for num in nums:
            if num - 1 not in seen:
                length = 0
                val = num
                while val in seen:
                    length += 1
                    val += 1

                longest = max(longest, length)



        return longest