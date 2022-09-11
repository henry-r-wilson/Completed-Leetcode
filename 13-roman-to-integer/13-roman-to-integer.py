class Solution:
    def romanToInt(self, s: str) -> int:
        
        numbers = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        amount = 0
        
        for i in range(len(s)):
            if i + 1 < len(s) and numbers[s[i]] < numbers[s[i + 1]]:
                amount -= numbers[s[i]] 
            else:
                amount += numbers[s[i]]
    
        return amount
    
#This code makes a dictionary for all the numberical roman values, and their arabic counterparts. It then sets a varialbe 'amount' to 0, which is used for the answer. We then say that i in the range of the length of input 's', if i + 1 is less than the length of s (i.e Does it have a character that comes after it, makes sure it doesn't come out of bounds) and the value of the currently assessed number is less than the value of the next number, then subtract the currently assessed value from variable 'amount', and if not, add value to variable 'amount'. This works as roman numerals are always largest to smallest from left to right, with the only acception being when 4, 9, or it's higher order of magnitude equivalent. As such, we will never have a mistake where it does VD (5 and 500) and come out with a -5 because VD isn't a valid roman number. This would instead be DV, and in that case D > V so it becomes 505 instead of 495.  
            
#numbers = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000} - Creates a dictionary of all relevant numbers from roman numerals to arabic numerals

#amount = 0 - Creates a varialbe for later use in the answer
        
#for i in range(len(s)): - States that for all values in the string 's', do action

#if i + 1 < len(s) and numbers[s[i]] < numbers[s[i + 1]]: - States that if number is within range of string 's' and the next number in the string is greater than the current number, do action

#amount -= numbers[s[i]] - Action is that the current number in the string should be subtracted from 'amount', and then set amount to be equal to this subtraction 
            
#else: - If above statement is not true, do action

#amount += numbers[s[i]] - Action is that the current number in the string should be added to 'amount', and then set amount to be equal to this subtraction 
    
#return amount - Return the value of 'amount' once for loop is completed.    
            