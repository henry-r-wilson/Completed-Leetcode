class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        value = []
        for i in range(1, n + 1): 
            if i%5 == 0 and i%3 == 0: 
                value.append('FizzBuzz') 
            elif i%3 == 0:
                value.append('Fizz')
            elif i%5 == 0:
                value.append('Buzz')
            else:
                value.append(str(i))
        return value
    
#By making a string for the final result, we can have the numbers in the range of n scanned and, if divisisble by both 5 and 3, return FizzBuzz. If only 3, then return Fizz and if only 5, return Buzz. If none of the above, return the string of the integer. The values are appended to the string "value" after the n has been successfully scanned.

#LINE BREAKDOWN

#value = [] - Makes string to use in final answer

#for i in range(1, n + 1): - Makes an if statement to scan through the range of integer n. In this case since we want to start at 1 instead of 0, we put a '1' initially to say to Python "Start on the second number in the range". 1 is used instead of 2, because Python starts all series of numbers at 0 as it's first (1) input. We then add '+ 1' to the 'n', as Python has been told to scan the first 3 values, but skip 0, so without the '+ 1' it would only scan the next two.

#if i%5 == 0 and i%3 == 0: - States that if i is divisible by 5 or divisible by 3, do action

#value.append('FizzBuzz') - Appends 'FizzBuzz' into the prior made string 
            
#elif i%3 == 0: - States that if i is divisible by 3, do action
                
#value.append('Fizz') - Appends 'Fizz' into the prior made string
            
#elif i%5 == 0: - States that if i is divisible by 5, do action
                
#value.append('Buzz') - Appends 'Buzz' into the prior made string
            
#else: - States that if i is not divisible by 3 or 5, do action
                
#value.append(str(i)) - Appends the string of the integer 'i' into the prior made string. We have to use str(i) as all the FizzBuzz's are constant, so can be noted string using '' but since the integer changes, 'i' would return i instead of the value of i. Therefore, str(i) is used.
        
#return value - Returns the string 'value' filled with all the appends made in the if loop 
            
            
            
        