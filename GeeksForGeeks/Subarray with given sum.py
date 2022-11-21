# User function Template for python3

# Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self, arr, n, s):
        # Write your code here
        start = 0
        sub = []
        flag = 0
        temp = 0
        for i in range(n):
            temp += arr[i]
            while(temp > s):
                temp -= arr[start]
                start += 1
            if temp == s and s!=0:
                sub.extend([start + 1, i + 1])
                flag = 1
                break
        if flag == 0:
            sub.append(-1)
        return sub


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