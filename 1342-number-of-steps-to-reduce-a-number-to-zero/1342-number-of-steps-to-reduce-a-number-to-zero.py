class Solution:
    def numberOfSteps(self, num: int) -> int:
        
        steps = 0
        
        while num:
            if num%2 == 0:
                 num //= 2
            else:
                num -= 1
            steps += 1
        return steps

#Initially creating a step variable at 0. we state that while there is an exist number (i.e. a non-zero number), if that numbers remainder after dividing by 2 is 0 (an even number), then divide that number by 2 and make it the new value of num. If the remainder of the number is non-zero (an odd number), then subtract 1 from the number and make that the new number instead. For each step that num is still a number, add 1 to the amount of steps taken. When num isn't a number anymore (i.e = 0), stop the while loop and return the number of steps taken. 

#LINE BREAKDOWN

#class Solution: - Creates a class for the solutions
    
#def numberOfSteps(self, num: int) -> int: - Defines the number of steps taken as an integer
        
#steps = 0 - Creates a varialbe for the steps taken
        
#while num: - Creates a "while loop" which says that while number is number, keep going. This can also be achieved with "while num != 0", where != means "is not".

#if num%2 == 0: - States that if the remainder of num / 2 = 0, do action. In this case, "%" means "remainder after division" 
                 
#num //= 2 - Action of if statement. Makes num be divided by 2, and then sets num to equal this division. The same can be achieved with "num = num // 2" where "//" means "divide, and then remove decimal places". "//=" means "divide, remove decimal places, and then make value equal division".
            
#else: - If the "if" statement is false, i.e. num%2 doesn't equal 0, do this action instead.

#num -= 1 - Action of else statement. Makes num be subtracted by 2, and then sets num to equal this subtraction. The same can be achieved with "num = num - 1". "-=" means "subtraction, and then make value equal subtraction".
             
#steps += 1 - Adds a step for each loop completed. "+=" means "Add 1 to step", if we make it "+= 2", then it would add 2 with each step.
        
#return steps - Once while loop is complete, return the number of steps taken.
                
        
