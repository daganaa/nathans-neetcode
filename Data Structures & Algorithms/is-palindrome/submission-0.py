class Solution:
    def isPalindrome(self, s: str) -> bool:
        rs = ""
        for c in s:
            if c.isalnum():
                rs += c.lower()
        
        l, r = 0, len(rs) - 1
        while l < r:
            if rs[l] != rs[r]:
                return False
            l += 1
            r -= 1
        return True