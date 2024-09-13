class Solution:
    def twoSum(self, nums, target: int):
        # x + y = target
        # x = target - y
        # if x exists in out set/map
        # we found the satisfying element so return the index
        map = {}
        for idx, value in enumerate(nums):
            x = target - value
            if x in map:
                return [map[x], idx]
            map[value] = idx
        return []
                
        
        
instance = Solution()
print(instance.twoSum([1,2,4,5],6))