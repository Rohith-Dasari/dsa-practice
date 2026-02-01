#REQUIREMENTS
#given an array of integers
#find max possible profit

#approach
#max +ve diff 
#find min price and update max profit according to the next profit  it gained

arr=[1,-3,5,7,9]
#maximum subarray sum
def maxSubArray(nums: list[int]) -> int:
    current=nums[0]
    best=nums[0]
    for num in nums[1:]:
        current=max(num,current+num)
        best=max(current,best)
    return best

def best_time_to_sell_stock(prices):
    min_price = float("inf")
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)

    return max_profit


print(maxSubArray([1,2,-1,4,-3]))
print(best_time_to_sell_stock([-1,-2,-1,-4,-3]))
        
    