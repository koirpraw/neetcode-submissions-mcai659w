class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        else:
            return True 


my_solution = Solution()
my_solution.hasDuplicate([1,2,3,3])