class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minimum = min(nums)
        ans = 0

        for x in nums:
            ans += x - minimum

        return ans