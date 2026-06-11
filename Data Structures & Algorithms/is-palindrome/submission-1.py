class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-z0-9]', '', s)
        reversed_string = s[::-1]

        if reversed_string == s:
            return True
        else:
            return False
        