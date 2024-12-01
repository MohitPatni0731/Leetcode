# https://leetcode.com/contest/weekly-contest-426/problems/smallest-number-with-all-set-bits/description/

class Solution:
    def smallestNumber(self, n: int) -> int:
        def binary(n):
            if n == 0:
                return "0"
            
            bina = ""
            while n > 0:
                bina = str(n % 2) + bina
                n //= 2
            
            return bina
        
        for i in range(n, n+10000):
            if '0' not in binary(i):#[2:]:
                return i
                break
