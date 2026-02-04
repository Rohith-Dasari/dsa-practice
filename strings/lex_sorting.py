
#bubble sort
def lexographic_sort(s:str):
    s_list=list(s)
    for i in range(len(s_list)):
        curr= s_list[i]
        for j  in range(i+1,len(s_list)):
            if curr>s[j]:
                s_list[i],s_list[j]=s_list[j],s_list[i]
        
    return "".join(s_list)


#merge_sort
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left,right)
def merge(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
        result.extend(left[1:])
        result.extend(right[j:])
    return result
def merge_lex_sort(s:str):
    v=merge_sort(list(s))
    return "".join(v)
        
print(lexographic_sort("zyx"))