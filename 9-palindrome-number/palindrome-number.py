class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        for i in range(len(s)//2):
            if s[i] == s[-i - 1]:
                pass
            else:
                return False
        return True
