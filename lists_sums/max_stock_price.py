#REQUIREMENTS
#given an array of integers
#find 2 points - when to buy and sell

#approach
#max +ve diff 

arr=[1,-3,5,7,9]
#maximum subarray sum
def maxSubArray(nums: list[int]) -> int:
    current=nums[0]
    best=nums[0]
    for num in nums[1:]:
        current=max(num,current+num)
        best=max(current,best)
    return best

def best_time_to_sell_stock(nums:list):
    best=nums[0]
    curr=nums[0]
    for num in nums[1:]:
        curr=max(num,curr+num)
        best=max(best,curr)
    return best if best>0  else 0

print(maxSubArray([1,2,-1,4,-3]))
print(best_time_to_sell_stock([-1,-2,-1,-4,-3]))
        
    