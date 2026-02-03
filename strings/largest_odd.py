class Solution:
    def largestOddNumber(self, num: str) -> str:
        for idx in range(len(num)-1,-1,-1):
            if num[idx] in {"1","3","5","7","9"}:
                return num[:idx+1]
        return ""

        