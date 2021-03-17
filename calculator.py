"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

# repeat forever 
while True:
#     tokenize string
    user_choice = input("> ")
    user_choice = user_choice.split(' ')
#     if its not equal to q
    if user_choice[0] == 'q':
#      end program 
        print("Exiting Program")
        break
    else:
        num1 = int(user_choice[1])
        if len(user_choice) < 2: 
            num2 = int(user_choice[2])
#     check what operation the first item in the list is equal together  
#         then perform the operation with the 2nd and 3rd item in the list\
        if user_choice[0] == "+":
            print(add(num1,num2))

        elif user_choice[0] == "-":
            print(subtract(num1, num2))    

        elif user_choice[0] == "*":
            print(multiply(num1,num2))

        elif user_choice[0]== "/":
            print(divide(num1,num2))

        elif user_choice[0]== "square":
            print (square (num1))

        elif user_choice[0]== "cube":
            print (cube(num1))

        elif user_choice[0] =="pow":
            print (pow(num1, num2))

        elif user_choice[0] == "mod":    
            print(mod(num1,num2))

        else: 
            print( "Wrong option")        

