class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        locs = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    locs.append(i)
                    locs.append(j)
        return locs
 


        