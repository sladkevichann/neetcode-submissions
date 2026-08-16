class Solution:

    def encode(self, strs: List[str]) -> str:
        resstr = [] #для производительности потом превратишь в строку бляя тк иммьютабл
        for s in strs:
            resstr.append(str(len(s)))
            resstr.append("#")
            resstr.append(s)
        return "".join(resstr) # brinfing lest into a string w no separator

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            n = []
            while s[i] != "#":
                n.append(s[i])
                i += 1
            res.append(s[i + 1:1 + i + int("".join(n))])
            i += int("".join(n)) + 1
            n = []
        
        return res
