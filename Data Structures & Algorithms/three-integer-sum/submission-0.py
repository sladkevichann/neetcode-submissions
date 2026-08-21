class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # complexity nlog(n) - for duplicates
        freqdict = defaultdict(int)
        for num in nums:
            freqdict[num] += 1 
        
        res = []
        for i in range(len(nums)):
            freqdict[nums[i]] -= 1 # временно откл - как и где потом вкл?
            if i and nums[i] == nums[i - 1]: # нулевой индекс не включается тк -1 это не дубликат конечно же
                continue # убираем дубликаты

            for j in range(i + 1, len(nums)): # шаг не обязателен
                freqdict[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]: # убираем дубликаты, но не сравниваем с i
                    continue
                target = - (nums[i] + nums[j])
                if freqdict[target] > 0:
                    res.append([nums[i], nums[j], target])
            
            for j in range(i + 1, len(nums)):
                freqdict[nums[j]] += 1 # добавляем обратно frequencies, но только не i тк с ним уже все прошерстили

        return res


        