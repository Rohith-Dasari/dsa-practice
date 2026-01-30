#REQUIREMENTS
#reverse an array
#no extra space to be used

def reverse_in_place(arr:list):
    left=0
    right=len(arr)-1
    
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr
print(reverse_in_place([1,2,3,4,5]))

