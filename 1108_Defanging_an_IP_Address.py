class Solution:
    # def defangIPaddr(self, address: str) -> str:
    #      return '[.]'.join(address.split('.'))

    # def defangIPaddr(self, address: str) -> str:
    #     r = ""
    #     for i in address:
    #         if i == ".":
    #             r += "[.]"
    #         else:
    #             r += i
    #     return r

    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


print(Solution().defangIPaddr("1.1.1.1"))
print(Solution().defangIPaddr("255.100.50.0"))
