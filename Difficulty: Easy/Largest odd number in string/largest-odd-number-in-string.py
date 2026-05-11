class Solution:
    def maxOdd(self, s):
        n = len(s)
        
        for i in range(n-1,-1,-1):
            if s[i] in { '1','3','5','7','9'}:
                return s[:i+1]
        return ''