class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # защита от дуркаов
        if len(s) != len(t):
            return False
            
        hashTable1, hashTable2 = {}, {} # simple def
        for i in range(len(s)): # instead of 2 for loops
            hashTable1[s[i]] = hashTable1.get(s[i], 0) + 1 # string[index] = character at index place
            hashTable2[t[i]] = hashTable2.get(t[i], 0) + 1
        return hashTable1 == hashTable2
        