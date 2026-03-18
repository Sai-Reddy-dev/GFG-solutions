class Solution:
    def find(self, arr, x):
        # code here
        def lowerbound(arr,n,x):
            low = 0
            high = n-1
            ans = n
            
            while low <= high:
                mid = (low + high) // 2
                
                if arr[mid] >= x:
                    ans = mid
                    high = mid-1
                elif arr[mid] < x:
                    low = mid+1
                else:
                    high = mid - 1
            return ans
        
        def upperbound(arr,n,x):
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
        
        n= len(arr)
        lb = lowerbound(arr,n,x)
        if (lb == n or arr[lb] != x):
            return [-1,-1]
        else:
            return [lb,(upperbound(arr,n,x))]
                    