class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        max = len(s) - 1 
        alphanumeric = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        start = 0
        back = - 1
        while (start <= max) or (back >= -max-1):
            while start <= max-1 and not (s[start] in alphanumeric):
                start += 1
            while back >= -max-1  and not (s[back] in alphanumeric):
                back -= 1
            if (start <= max) and (back >= -max-1) and (s[start] != s[back]):
                return False
            start += 1
            back -= 1
        return True


        