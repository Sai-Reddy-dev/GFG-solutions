class Solution:
    
    def can_we_place(self,arr,dist,cows):
        cntcows = 1
        lastcow = arr[0]
        
        for i in range(1,len(arr)):
            if arr[i] - lastcow >= dist:
                cntcows += 1
                lastcow = arr[i]
        return cows <= cntcows
        
    def aggressiveCows(self, stalls, k):
        # code here
        stalls.sort()
        low = 1
        high = max(stalls)
        ans = 1
        while(low <= high):
            mid = (low + high) // 2
            
            if self.can_we_place(stalls,mid,k):
                low = mid +1
                ans = mid
            else:
                high = mid -1
        return ans