anagram_list=["abt","tab","eat","ate","bat"]
#return anagrams grouped in tuples

def group_anagram(al:list[str])->list[tuple[str]]:
    a_map={}
    for word in al:
        key="".join(sorted(word))
        if key in a_map.keys():
         a_map[key].append(word)
        else:
            initial_list=[word]
            a_map[key]=initial_list
    result=[]
    for key,value in a_map.items():
        group=tuple(value) 
        result.append(group)
    return result
print(group_anagram(anagram_list))

        
        
        
    