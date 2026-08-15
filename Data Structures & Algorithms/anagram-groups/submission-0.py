class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # dict w values as lists for default
        for s in strs:
            zeroslist = [0] * 26 # just 26 zeros
            for c in s:
                zeroslist[ord(c) - ord('a')] += 1
            res[tuple(zeroslist)].append(s)
        return list(res.values())

        
        