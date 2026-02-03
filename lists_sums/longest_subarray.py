# Given an array of integers and a number K, 
# find the length of the longest contiguous subarray whose sum equals K.
# Positive numbers only → sliding window

# Mixed positives & negatives → prefix sum + hash map

def finder(nums:list):
    nums=sorted(nums)
    