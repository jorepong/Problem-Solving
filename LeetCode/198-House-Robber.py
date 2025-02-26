class Solution:
    def rob(self, nums: List[int]) -> int:
        house = [nums[0]]
        maximum = house[0]

        for i in range(1, len(nums)):
            if i-3 >= 0:
                house.append(max(house[i-2] + nums[i], house[i-3] + nums[i]))
            elif i-2 >= 0:
                house.append(house[i-2] + nums[i])
            else:
                house.append(nums[i])

            maximum = max(maximum, house[i])

        return maximum