class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        dup = sorted(nums)
        for i in range(n):
            last = nums[-1]
            for j in range(n-1,0,-1):
                nums[j] = nums[j-1]
            nums[0]= last
            if dup == nums:
                return True
        return False