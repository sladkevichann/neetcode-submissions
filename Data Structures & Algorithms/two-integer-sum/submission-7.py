class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap in python is a dictionary O(1) lookup
        hashtable = {} # val -> index

        for i in range(len(nums)):
            # 1
            complement = target - nums[i]
            if (complement in hashtable) and (i != hashtable[complement]):
                return [hashtable[complement], i] # тут не волнуйся насчет мин макс тк мы интерируем с минимального индекса по самый старший и complement всегда будет меньшим
            # 2 order matters чтобы не затирать дубликаты при прокладке в hastable (nums=[5,5])
            hashtable[nums[i]] = i # если не существует пары, вот так на похуй задаем ее по key