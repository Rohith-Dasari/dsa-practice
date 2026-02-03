
def reverseWords(s: str) -> str:
    words=s.split()
    reverse_words=words[::-1]
    return " ".join(reverse_words)

def reverseWords(s: str) -> str:
    result=[]
    idx=len(s)-1
    while idx>=0:
        word=[]
        while idx>=0 and s[idx]==" ":
            idx-=1
        while idx>=0 and s[idx]!=" ":
            word.append(s[idx])
            idx-=1
        if word:
            word=reversed(word)
            result.append("".join(word))
    return " ".join(result)
           
