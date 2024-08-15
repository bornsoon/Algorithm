class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == len(set(s)):
            MAX = len(s)
        else:
            MAX = 0
            for x in range(len(s)):
                temp = [] 
                set_s = set(s)
                for i in s[x:]:
                    if i in set_s:
                        set_s.remove(i)
                        temp.append(i)
                        MAX = max(MAX, len(temp))
                    else:
                            break
        return MAX
