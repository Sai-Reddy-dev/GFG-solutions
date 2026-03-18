class Solution:
    def findFloor(self, arr, x):
        # code here
        n = len(arr)
        low = 0
        high = n-1
        ans = -1
        while low <= high:
            
            mid = (low + high) // 2
            
            if arr[mid] <= x:
                ans = mid
                low  = mid + 1
            else:
                high = mid  - 1
        return ans
        