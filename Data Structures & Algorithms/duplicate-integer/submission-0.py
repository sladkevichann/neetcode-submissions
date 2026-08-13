class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for n in nums:
            if not (n in hashSet):
                hashSet.add(n)
            else:
                return True
        return False
        