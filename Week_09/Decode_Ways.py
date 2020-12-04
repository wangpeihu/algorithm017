class Solution:

    '''
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        pre = curr = 1
        size_s = len(s)
        for i in range(1, size_s):
            tmp = curr
            if s[i] == '0':
                if s[i - 1] == '1' or s[i - 1] == '2':
                    curr = pre
                else:
                    return 0
            else:
                if (s[i - 1] == '1') or (s[i - 1] == '2' and 1 <= int(s[i]) <= 6):
                    curr = curr + pre
            pre = tmp
        return curr
    '''
    def numDecodings(self, s: str) -> int:
        size_nums = len(s)
        dp = [0] * (size_nums + 1)
        dp[size_nums] = 1
        if s[size_nums - 1] != '0':
            dp[size_nums - 1] = 1
        for i in range(size_nums - 2, -1, -1):
            if s[i] == '0':
                continue
            if '1' <= s[i] <= '9':
                dp[i] = dp[i + 1]
            if '10' <= s[i:i + 2] <= '26':
                dp[i] = dp[i + 1] + dp[i + 2]
        return dp[0]