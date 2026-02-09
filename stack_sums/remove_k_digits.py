class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        stack=[]
        for num in nums:
            while stack and k>0 and stack[-1]>num:
                k-=1
                stack.pop()

            stack.append(num)
        while k>0:
            stack.pop()
            k-=1
        res="".join(stack)
        res=res.lstrip("0")
        return res if res else "0"
