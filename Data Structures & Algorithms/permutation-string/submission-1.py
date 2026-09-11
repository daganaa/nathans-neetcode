class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ln = len(s1)
        st1 = sorted(s1)

        for i in range(len(s2) - ln + 1):
            sub = s2[i:(i+ln)]
            st2 = sorted(sub)
            if st1 == st2:
                return True
        return False
