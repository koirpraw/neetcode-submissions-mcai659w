class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_cased = s.lower()
        edited = ''.join(filter(str.isalnum,lower_cased))
        reversed = edited[::-1]
        if edited == reversed:
            return True
        else:
            return False