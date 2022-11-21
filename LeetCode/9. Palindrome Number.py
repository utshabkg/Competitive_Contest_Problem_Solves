class Solution:
    def isPalindrome(self, x: int) -> bool:

        flag = True
        if x < 0:
            return False

        new = ''
        x_2 = x
        while x_2 > 0:
            new += str(x_2 % 10)
            x_2 = x_2 // 10

        print(new)
        if int(new) == x:
            return True
        else:
            return False


print(Solution().isPalindrome(121))
print(int('01'))
