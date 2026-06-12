class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        place = 1

        while place <= n:
            high = n // (place * 10)
            cur = (n // place) % 10
            low = n % place

            if cur == 0:
                count += high * place
            elif cur == 1:
                count += high * place + low + 1
            else:
                count += (high + 1) * place

            place *= 10

        return count