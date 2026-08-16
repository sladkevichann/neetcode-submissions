class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        n = 1
        for num in nums:
            n *= num
            prefix.append(n)
        n = 1
        for i in range(len(nums) - 1, 0, -1): # 0 не включительно (end) always bc manually doing thoseee
            n *= nums[i]
            suffix.append(n)
        res = []
        res.append(suffix[-1])
        for i in range(1, len(nums) - 1, 1):
            res.append(prefix[i - 1] * suffix[len(nums) - i - 2])
        res.append(prefix[-2])
        return res
        