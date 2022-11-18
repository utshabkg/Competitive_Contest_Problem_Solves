# User function Template for python3

# Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self, arr, n, s):
        # Write your code here
        sub = []

        for i in range(n):
            if len(sub)==2:
                break
            temp = arr[i]
            if temp == s:
                sub.append(i + 1)
                sub.append(i + 1)
                break

            for j in range(i+1, n):
                temp += arr[j]
                if temp == s:
                    sub.append(i + 1)
                    sub.append(j + 1)
                elif temp > s:
                    break
                else:
                    pass

        # print(sub)
        if len(sub) == 2:
            return sub
        else:
            return [-1]


# {
# Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        NS = input().strip().split()
        N = int(NS[0])
        S = int(NS[1])

        A = list(map(int, input().split()))
        ob = Solution()
        ans = ob.subArraySum(A, N, S)

        for i in ans:
            print(i, end=" ")

        print()

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends