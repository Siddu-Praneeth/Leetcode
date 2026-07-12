from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        sorted_arr = sorted(set(arr))

        r = 1
        for num in sorted_arr:
            rank[num] = r
            r += 1

        ans = []
        for num in arr:
            ans.append(rank[num])

        return ans