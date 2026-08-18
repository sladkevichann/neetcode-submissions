class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        start = 0
        back = len(s) - 1
        while start < back:
            while start < back and not (s[start].isalnum()):
                start += 1
            while start < back and not (s[back].isalnum()):
                back -= 1
            if  s[start] != s[back]:
                return False
            start += 1
            back -= 1
        return True


        