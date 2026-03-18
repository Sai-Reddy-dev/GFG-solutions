class Solution:
    def countFreq(self, arr, x):
        # code here
        def frist(arr,n,x):
            low = 0
            high = n-1
            ans = -1
            
            while low <= high:
                mid = (low + high) // 2
                
                if arr[mid] == x:
                    ans = mid
                    high = mid-1
                elif arr[mid] < x:
                    low = mid+1
                else:
                    high = mid - 1
            return ans
        
        def last(arr,n,x):
            low = 0
            high = n-1
            ans = -1
            
            while low <= high:
                mid = (low + high) // 2
                
                if arr[mid] ==  x:
                    ans = mid
                    low = mid +1
                elif arr[mid] < x:
                    low = mid +1
                else:
                    high = mid -1
            return ans
        
        n = len(arr)
        frist = frist(arr,n,x)
        last = last(arr,n,x)
        
        if frist == -1:
            return 0
        else:
            return (last - frist) + 1
        