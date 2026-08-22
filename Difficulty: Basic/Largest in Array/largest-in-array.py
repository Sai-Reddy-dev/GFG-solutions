class Solution:
    def largest(self, arr):
        # code here
        large = arr[0]
        
        for i in range(1,len(arr)):
            if large < arr[i]:
                large = arr[i]
        return large
