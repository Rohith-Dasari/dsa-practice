def ast_coll(asteroids:list):
    stack=[]
    for asteroid in asteroids:
        while stack and stack[-1]>0 and asteroid<0 and stack[-1]<abs(asteroid):
                stack.pop()
        if stack and stack[-1]>0 and asteroid<0 and stack[-1]==abs(asteroid):
            stack.pop()
            continue
        elif stack and stack[-1]>0 and asteroid<0 and stack[-1]>abs(asteroid):
            continue
        stack.append(asteroid)
    return stack

print(ast_coll([3,5,-6,2,-1,4]))