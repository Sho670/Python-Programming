class Solution:
    def numSubArray(self, nums: list[int], k: int):
        if k<=1:
            return 0
        count = 0
        product = 1
        left = 0
        for right in range(len(nums)):
            product *= nums[right]

            while product >= k and left <= right:
                product //=nums[right]
                left+=1

            count += right-left+1
        return count
        