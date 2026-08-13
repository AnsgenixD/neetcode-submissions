class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_in_s = {}
        seen_in_t={}
        for i in s:
            seen_in_s[i]= seen_in_s.get(i,0) +1
        for n in t:
            seen_in_t[n]= seen_in_t.get(n,0) +1
        if seen_in_s == seen_in_t:
            return True
        return False
        