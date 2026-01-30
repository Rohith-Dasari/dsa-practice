#REQUIREMENTS
# given a  sorted  array
# return [idx1,idx2] such that
#values at those indices add to target


#approach
#use two pointer at start and end
# if target is lesser then sum of pointer valuees, decrement right
# if bigger,  increment left
#if found return sum

def two_sum_sorted(arr:list,target:int):
    left=0
    right=len(arr)-1
    while left<right:
        sum=arr[left]+arr[right]
        if sum==target:
            return [left,right]
        elif sum>target:
            right-=1
        elif sum<target:
            left+=1
    return None

def two_sum_sorted_return_all_pairs(arr:list,target:int):
    left=0
    right=len(arr)-1
    result=[]
    while left<right:
        curr_sum=arr[left]+arr[right]
        if curr_sum==target:
            result.append((left,right))
            
            while left<right and arr[left]==arr[left+1]:
                left+=1
            left+=1
            while right>left and arr[right]==arr[right-1]:
                right-=1
            right-=1
        elif curr_sum>target:
            right-=1
        elif curr_sum<target:
            left+=1
    return result or None
