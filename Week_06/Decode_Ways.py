class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        size = len(s)
        pre = curr = 1
        for i in range(1, size):
            tmp = curr
            if s[i] == '0':
                if s[i - 1] == '1' or s[i - 1] == '2':
                    curr = pre
                else:
                    return 0
            else:
                if (s[i - 1] == '1') or (s[i - 1] == '2' and 1 <= int(s[i]) <= 6):
                    curr += pre
            pre = tmp
    
        return curr