from typing import List


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        # 5 precision po
        return [celsius + 273.15, celsius * 9 / 5 + 32]


print(Solution().convertTemperature(36.50))
print(Solution().convertTemperature(122.11))
