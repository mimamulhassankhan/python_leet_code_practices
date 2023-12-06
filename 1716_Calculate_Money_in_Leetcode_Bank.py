class Solution:
    def totalMoney(self, n: int) -> int:
        STEP = 7
        BASE = 28
        DIVIDE = n // STEP
        REMAINDER = n % STEP
        STOP = BASE + STEP * DIVIDE
        START_SEQUENCE_AT = DIVIDE + 1
        END_SEQUENCE_AT = DIVIDE + REMAINDER

        sum_of_steps = sum(
            [
                sum(i for i in range(BASE, STOP, STEP)),
                ((START_SEQUENCE_AT + END_SEQUENCE_AT) * REMAINDER) // 2,
            ]
        )
        return sum_of_steps


print(Solution().totalMoney(10))
