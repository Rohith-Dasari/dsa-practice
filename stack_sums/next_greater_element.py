from typing import List

#brute force approach
def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
        result=[0]*len(nums1)
        for idx,num in enumerate(nums1):
            for i,element in enumerate(nums2):
                if num==element:
                    for j in range(i+1,len(nums2)):
                        if nums2[j]>element:
                            result[idx]=nums2[j]
                            break
                    else:
                        result[idx]=-1
                    break
        return result
#part1
#MONOTONIC STACK
def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    stack = []
    next_greater = {}
    for i in range(len(nums2) - 1, -1, -1):
        num = nums2[i]
        while stack and stack[-1] <= num:
            stack.pop()
        next_greater[num] = stack[-1] if stack else -1
        stack.append(num)
    return [next_greater[num] for num in nums1]


#PART 2
#monotonic stack approach
def nextGreaterElements(nums: List[int]) -> List[int]:
    length=len(nums)
    nge_stack=[]
    result=[-1]*length
    for idx in range(2*length-1,-1,-1):
        element = nums[idx % length]
        while nge_stack and nge_stack[-1]<=element:
            nge_stack.pop()
        if idx<length:
            result[idx]=nge_stack[-1] if nge_stack else -1
        nge_stack.append(element)

    return result
print(nextGreaterElements([1,2,3,4,3]))
