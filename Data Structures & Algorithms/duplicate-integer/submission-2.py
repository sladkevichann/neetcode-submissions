class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set() # hash табличка(set) так обозначается просто
        for n in nums:
            if not (n in hashSet): # в питоне отрицание not
                hashSet.add(n) # добавляем в табличку
            else:
                return True
        return False
        