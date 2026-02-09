class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len=0
        streak=0
        for i in range(len(nums)):
            if nums[i]==1:
                streak+=1
            else:
                streak=0
            if streak>max_len:
                max_len=streak
        return max_len

        