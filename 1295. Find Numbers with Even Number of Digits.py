class Solution:
    def findNumbers(self, nums):
        even_digit_count = 0   
        
        for num in nums:
            # Count the number of digits by repeatedly dividing by 10
            digit_count = 0
            while num > 0:
                num //= 10
                digit_count += 1
            
            # Check if the digit count is even
            if digit_count % 2 == 0:
                even_digit_count += 1
                
        return even_digit_count
solution = Solution()
print(solution.findNumbers([12, 345, 2, 6, 7896])) 
