class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n

        product = nums[0]
        for i in range(1, n):
            prefix[i] = product
            product *= nums[i]

        # 1, 1, 2, 8

        # 48, 24, 6, 1

        ans = [0] * n

        product = 1
        for i in range(n-1,-1,-1):
            ans[i] = product * prefix[i]
            product *= nums[i]

        return ans