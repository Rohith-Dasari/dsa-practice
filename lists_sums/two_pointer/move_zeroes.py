#REQUIREMENTS
# given an array with 0s
#shift them to end
# no new array/copy should be made

#approach-1
#overwrite elements to where zeros with 2 pointers
# append the number of zeroes 
def move_zeroes(arr:list):
    left=0
    for idx in range(len(arr)):
        if arr[idx]!=0:
            arr[left]=arr[idx]
            left+=1
    for idx in range(left,len(arr)):
            arr[idx]=0
    return arr
print(move_zeroes([12,0,1,0,0,0,0,0,0]))