# this program ask the user to enter any negative integer number and Use a for loop, to display output in such a way that the number is printed, and all subsequent ascending numbers, until 0 is reached
number=int(input("enter a negative interger number: "))
sum = 0
while number<0:
    print(number,end=" ")
#calculating the sum
    sum += number
    number +=1
sum += 0
print( "=",sum)#this is for printing out the results
    
