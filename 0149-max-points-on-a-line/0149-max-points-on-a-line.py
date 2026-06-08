from collections import defaultdict

class Solution:
    def maxPoints(self, points):
        n = len(points)

        if n <= 2:
            return n

        ans = 0

        for i in range(n):
            slopes = defaultdict(int)

            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]

                if x1 == x2:
                    slope = "SIDD"
                else:
                    slope = (y2 - y1) / (x2 - x1)

                slopes[slope] += 1

            ans = max(ans, max(slopes.values(), default=0) + 1)

        return ans