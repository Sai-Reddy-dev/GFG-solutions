class Solution:
    def search(self, arr, key):
        # code here
        n = len(arr)
        low = 0
        high = n-1
        
        while low <= high:
            
            mid = (low + high) // 2
            
            if key == arr[mid]:
                return mid
            
            if (arr[low] <= arr[mid]):
                if(key >= arr[low] and arr[mid] > key):
                    high = mid -1
                else:
                    low = mid + 1
            else:
                if(arr[mid] < key and key <= arr[high]):
                    low = mid + 1
                else:
                    high = mid -1
            
                
        return -1