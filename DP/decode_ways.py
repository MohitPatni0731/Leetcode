# https://leetcode.com/problems/decode-ways/description/
# Approach - ya toh s[i] 1 se shuru ho tab valid banega ya phir s[i] agar 2 se shuru ho raha hai toh check karenge ki s[i+1] "0123456" main he ho kyoki phir 26 pe toh alphabets end ho jaate hai 

class Solution:
    def numDecodings(self, s: str) -> int:
        def f(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0

            res = f(i + 1)
            if i < len(s) - 1:
                if (s[i] == '1' or 
                   (s[i] == '2' and s[i + 1] in '0123456')):
                    res += f(i + 2)

            return res

        return f(0)

