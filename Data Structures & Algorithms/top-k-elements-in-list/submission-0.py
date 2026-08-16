class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqdict = {}
        buckets = [[] for i in range(len(nums) + 1)] # list of lists to group numbers by their frequency and acess easily
        for num in nums:
            freqdict[num] = freqdict.get(num, 0) + 1 # weird way of incrementing frequency... just so that 0 is accounted for
        for key, val in freqdict.items(): # iteration by key and value
            buckets[val].append(key)
        res = []
        for bucketind in range(len(buckets) - 1, 0, -1): #start, end, step
            for num in buckets[bucketind]:
                res.append(num)
                if len(res) == k:
                    return res


        