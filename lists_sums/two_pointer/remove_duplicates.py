#Requirements
#given a sorted array
#remove duplicates

def remove_duplicates_brute_force(arr:list):
    idx=0
    while idx<len(arr):
        pointer=idx+1
        while pointer<len(arr) and arr[idx]==arr[pointer]:
            pointer+=1
        if pointer<len(arr):
            arr=arr[:idx+1]+arr[pointer:]
        else:
            arr=arr[:idx+1]
        idx=pointer  
    return arr

#approach
# find next unique number
#overwrite it  to the next number

def remove_duplicates_2_pointer(arr:list):
    left=0
    for right in range(1,len(arr)):
        if arr[right-1]!=arr[right]:
            arr[left+1]=arr[right]
            left+=1       
    return arr[:left+1]

print(remove_duplicates_2_pointer([1,2,2,2]))

    