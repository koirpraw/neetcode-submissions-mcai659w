class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_cased = s.lower()
        edited = ''.join(filter(str.isalnum,lower_cased))
        return edited == edited[::-1]
   