class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        print("__name__", [stone in jewels for stone in stones])
        # conver to for loop
        for stone in stones:
            if stone in jewels:
                print("__if__", stone)
        #     print(stone in jewels)
        #     print([stone in jewels for stone in stones])
        #     print(sum(stone in jewels for stone in stones))
        #     print("====")

        return sum(stone in jewels for stone in stones)


print(Solution().numJewelsInStones("aA", "aAAbbbb"))
print(Solution().numJewelsInStones("z", "ZZ"))
