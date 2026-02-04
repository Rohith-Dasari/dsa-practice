class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        num = 0
        i=0
        length=len(s)
        max_value=2**31-1
        min_value=-1*2**31
        while i<length and s[i] == " ":
            i += 1
        if i<length and s[i] == "-":
            sign = -1
            i+=1
        elif i<length and s[i] == "+":
            i+=1 
        for idx in range(i, len(s)):
            char = s[idx]
            if ord(char) > 47 and ord(char) < 58:
                num = num * 10
                num += int(char)
                if sign * num > max_value: return max_value
                if sign * num < min_value: return min_value
            else:
                break
        num=num*sign     

        return num
