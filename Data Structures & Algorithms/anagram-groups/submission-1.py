class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for st in strs: 
            sort = ''.join(sorted(st))
            if sort in anagrams: 
                anagrams[sort].append(st)
            else:
                anagrams[sort] = [st]
        return list(anagrams.values())