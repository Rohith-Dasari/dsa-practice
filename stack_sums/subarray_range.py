#brute_force
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        #summation of  all max-min of subarray 
        summation=0
        for i in range(len(nums)):
            subarray=[nums[i]]
            max_el=subarray[0]
            min_el=subarray[0]
            for j in range(i+1,len(nums)):
                subarray.append(nums[j])
                max_el=subarray[-1] if subarray[-1]>max_el else max_el
                min_el=subarray[-1] if subarray[-1]<min_el else min_el
                diff=max_el-min_el
                summation+=diff
        return summation


#optimal-stack
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)

        def get_count(is_max):
            left = [0] * n
            right = [0] * n
            stack = []

            for i in range(n):
                while stack and (
                    nums[stack[-1]] < nums[i] if is_max else nums[stack[-1]] > nums[i]
                ):
                    stack.pop()
                left[i] = i - stack[-1] if stack else i + 1
                stack.append(i)

            stack.clear()

            for i in range(n - 1, -1, -1):
                while stack and (
                    nums[stack[-1]] <= nums[i] if is_max else nums[stack[-1]] >= nums[i]
                ):
                    stack.pop()
                right[i] = stack[-1] - i if stack else n - i
                stack.append(i)

            return sum(nums[i] * left[i] * right[i] for i in range(n))

        return get_count(True) - get_count(False)

        