class Solution:
    def getSecondLargest(self, arr):
        # code here
        n = len(arr)
        
        largest = -1
        second_largest = -1
        
        for i in range(n):
            if arr[i] > largest:
                second_largest = largest
                largest = arr[i]
            elif arr[i] > second_largest and arr[i] < largest:
                second_largest = arr[i]
            
        return second_largest