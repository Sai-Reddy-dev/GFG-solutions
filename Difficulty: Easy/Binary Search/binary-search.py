class Solution:
    def binarysearch(self, arr, x):
        # Code Here
        low = 0
        high = len(arr) - 1
        while low <= high:
    
            mid = low + (high - low) // 2
    
            if arr[mid] == x and arr[mid-1] != x: 
                return mid
    
            elif arr[mid] < x:
                low = mid + 1
    
            else:
                high = mid - 1

        return -1
