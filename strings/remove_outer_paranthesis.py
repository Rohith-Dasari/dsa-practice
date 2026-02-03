
def removeOuterParentheses(self, s: str) -> str:
    
    # stack=[]
    depth=0
    result=[]
    for val in s:
        if not depth:
            depth+=1
            continue
        if val=="(":
            depth+=1
            result.append(val)
        elif val==")":
            if depth==1:
                # stack.pop()
                depth-=1
                continue
            else:
                result.append(val)
                depth-=1

    return "".join(result)
    

        