#User function Template for python3
class Solution:
    def countTriplet(self, arr, n):
        # code here
        count = 0
        arr = sorted(arr)
        large_index = n - 1
        while large_index >= 0:
            start = 0
            end = large_index - 1
            while start < end:
                if arr[large_index] == arr[start] + arr[end]:
                    count += 1
                    break
                elif arr[large_index] > arr[start] + arr[end]:
                    start += 1
                else:
                    end -= 1
            large_index -= 1
        return count

#
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        arr = [int(x) for x in input().split()]

        ob = Solution()
        ans = ob.countTriplet(arr, n)
        print(ans)

# } Driver Code Ends