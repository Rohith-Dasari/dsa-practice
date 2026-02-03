class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        s_array=list(s)
        goal_array=list(goal)
        for _ in range(len(s)+1):
            if s_array==goal_array:
                return True
            item=s_array.pop()
            s_array=[item]+s_array
        return False
