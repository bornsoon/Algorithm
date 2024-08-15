class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        for x in range(len(s)):
            temp = [] 
            set_s = set(s)
            for i in s[x:]:
                if i in set_s:
                    set_s.remove(i)
                    temp.append(i)
                    if max < len(temp):
                        max = len(temp)
                else:
                        break
        return max