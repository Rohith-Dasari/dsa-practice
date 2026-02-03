class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        smallest_length=len(strs[0])
        smallest_word=strs[0]
        for word in strs:
            word_length=len(word)
            if word_length<smallest_length:
                smallest_length=word_length
                smallest_word=word
        result=[]
        for char in smallest_word:
            result.append(char)
            prefix="".join(result)
            for word in strs:
                if not word.startswith(prefix):
                    return prefix[:-1]
        return "".join(result)




        