class Solution:
    # Function to find the subarray with the maximum sum
    def findSubarray(self, arr):
    	# code here
    	n = len(arr)
    	
    	curr_sum = 0
    	max_sum = -1
    	start = 0
    	ans_start = -1
    	ans_end = -1
    	
    	for i in range(n):
    	    if arr[i] < 0:
    	        curr_sum = 0
    	        start = i+1
    	        
    	    else:
    	        curr_sum += arr[i]
    	        
    	        if curr_sum > max_sum:
    	            max_sum = curr_sum
    	            ans_start = start
    	            ans_end = i
    	        elif curr_sum == max_sum:
    	            if(i - start) > (ans_end - ans_start):
    	                ans_start = start
    	                ans_end = i
    	   
        if ans_start == -1:
            return [-1]
        
        return arr[ans_start:ans_end+1]
    	    