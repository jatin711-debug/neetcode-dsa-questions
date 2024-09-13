class Solution:
    def hasDuplicate(self, nums) -> bool:
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                return True
            dict[nums[i]] = 1
        return False
    


instance = Solution()

print(instance.hasDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 1, 10])) # True

            

         
         