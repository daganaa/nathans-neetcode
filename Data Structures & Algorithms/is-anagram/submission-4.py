class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = dict()
        for letter in s:
            if letter not in seen:
                seen[letter] = 1
            else:
                seen[letter] += 1
        for letter in t:
            if letter not in seen:
                return False
            seen[letter] -= 1
        print(seen)
        for val in seen.values():
            if val != 0:
                return False
        return True