class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seqlength = defaultdict(int) # отсутствующий ключ возвращает 0
        res = 0

        for num in nums:
            if not seqlength[num]:
                seqlength[num] = seqlength[num - 1] + seqlength[num + 1] + 1
                seqlength[num - seqlength[num - 1]] = seqlength[num] # координата самого левого элемента этой последовательности
                seqlength[num + seqlength[num + 1]] = seqlength[num] # координата самого правого элемента этой последовательности
                res = max(res, seqlength[num])
        return res