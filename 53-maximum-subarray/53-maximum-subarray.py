class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSub = nums[0]
        amount = 0
        
        for i in nums:
            if amount < 0:
                amount = 0
            amount += i
            maxSub = max(maxSub, amount)
        return maxSub
    
#For this code, we use a makeshift 'sliding barrier' that will remove the first number in the subarray if it is negative. From here, if the first number is positive, add the value to 'amount'. Then, we use the max function to calculate the maximum value from the array from maxSub to amount.

#maxSub = nums[0] - Setting the maxSub value to be the first number in the list

#amount = 0 - Setting a varialbe 'amount' to equal 0

#for i in nums: - For all values in the list, do action

#if amount < 0: - If the first amount is less than 0, do action

#amount = 0: - Action is to reset the amount to 0

#amount += i - If the first number in the sequence is still positive, add the number to the amount

#maxSub = max(maxSub, amount) - Set maxSub to be the maximum amount possible from maxSub to amount

#return maxSub - Return the value for the maxSub

            
        