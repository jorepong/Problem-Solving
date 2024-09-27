import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = collections.defaultdict(int)

        for num in nums:
            map[num] += 1

        sorted_map = sorted(map.items(), key=lambda item: item[1], reverse=True)

        result = []
        for i in range(k):
            result.append(sorted_map[i][0])

        return result