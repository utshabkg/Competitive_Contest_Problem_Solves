"""
Given a array of integers , find 3 indexes i,j,k such that,
i<j<k and a[i] < a[j] < a[k]. Best possible is a O(n) algorithm.
"""

def getijk(array):
    result = []
    count = 0
    for item in array:
        result.append([item])
        for result_item in result:
            if(len(result_item) == 3):
                print(result_item)
                result.remove(result_item)
                count += 1
            elif (item > result_item[-1]):
                a = result_item[:]
                a.append(item)
                result.append(a)
    print(count)

if __name__ == "__main__":
    array = [2,1,4,5,7]
    getijk(array)
     
    # array = [4,7,5,1,3,8,9,6,2]
    # getijk(array)