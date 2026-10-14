class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()


        i = 0

        for i, num in enumerate(nums[:-2]):

            if i > 0 and num == nums[i-1]:
                continue
            
            if nums[i] > 0:
                break

            target = -(nums[i])
            j = i + 1
            k = n-1

            while j < k:
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    curr = nums[j]
                    while j < k and nums[j] == curr:
                        j += 1
                    k-=1
            
            # curr = nums[i]
            # while i < k and nums[i] == curr:
            #     i += 1
            i += 1

        return ans

