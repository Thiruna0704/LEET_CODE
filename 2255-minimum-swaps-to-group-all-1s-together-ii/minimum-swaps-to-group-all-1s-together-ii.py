class Solution(object):
    def minSwaps(self, nums):
        
        n = len(nums)
        
        
        total_ones = sum(nums)
        
        
        if total_ones == 0 or total_ones == n:
            return 0
        
      
        current_ones = sum(nums[:total_ones])
        max_ones_in_window = current_ones
        
        
        for i in range(1, n):
            
            leaving_element = nums[i - 1]
           
            entering_element = nums[(i + total_ones - 1) % n]
            
            
            current_ones += entering_element - leaving_element
            
            
            max_ones_in_window = max(max_ones_in_window, current_ones)
            
        
        return total_ones - max_ones_in_window