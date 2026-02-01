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

#monotonic stack approach
