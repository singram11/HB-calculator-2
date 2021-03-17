"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

# repeat forever 
while True:
#     tokenize string
    user_choice = input("> ")
    user_choice = user_choice.split(' ')
    print(user_choice)
#     if its not equal to q
    if user_choice[0] == 'q':
#      end program 
        print("Exiting Program")
        break
    else:
        num1 = int(user_choice[1])
        num2 = int(user_choice[2])
#     check what operation the first item in the list is equal together  
#         then perform the operation with the 2nd and 3rd item in the list\
        if user_choice[0] == "+":
            print(add(num1,num2))
            

