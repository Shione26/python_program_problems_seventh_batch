# Prog09. index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.

# ask the user for input
text = input("Enter text: ")
# ask the user what character to find
character = input("Enter character to find: ")
# initialize position as -1 if the character is not found
position = -1
# initialize index as 0
index = 0
# check each character if it match the character to find
# if no, increment index variable until character is found
# if yes, set the position to the current index then break
# print the position