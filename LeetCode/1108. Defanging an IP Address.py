class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged = ""
        for a in address:
            if a == ".":
                defanged += "[.]"
                continue

            defanged += a

        return defanged