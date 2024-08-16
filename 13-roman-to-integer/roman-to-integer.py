class Solution:
    sum = 0
    sub = 0
    def romanToInt(self, s: str) -> int:
        romanDic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in s:
            self.sum = self.sum + romanDic[i]
            if (self.sub == 1 and i in ['V', 'X']) or (self.sub == 10 and i in ['L', 'C']) or (self.sub == 100 and i in ['D', 'M']):
                self.sum = self.sum - 2 * self.sub
            if i in ['I', 'X', 'C']:
                self.sub = romanDic[i]
        return self.sum