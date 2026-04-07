class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            anagram = ''.join(sorted(word))
            if anagram in anagrams:
                anagrams[anagram].append(word)
            else:
                anagrams[anagram] = [word]
        return list(anagrams.values())