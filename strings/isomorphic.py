class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map={}
        values=set()
        for idx in range(len(s)):
            s_char=s[idx]
            t_char=t[idx]
            if s_char in char_map:
                s_char=char_map[s_char]
            else:
                if t_char in values:
                    return False
                values.add(t_char)
                if s_char==t_char:
                    char_map[s_char]=s_char
                else:
                    char_map[s_char]=t_char
                    s_char=t_char
            if s_char!=t_char:
                return False
        return True



        