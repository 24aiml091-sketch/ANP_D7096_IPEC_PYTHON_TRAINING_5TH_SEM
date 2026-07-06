# Program to ask for the user's name and print the first name without using library functions
# Input the full name from the user
full_name = input("Enter your full name: ")

first_name = ""
started = False

# Iterate through each character in the string
for char in full_name:
    # If the character is a space (or other whitespace)
    if char == ' ' or char == '\t':
        if started:
            # Stop if we already started collecting characters of the first name
            break
    else:
        # Append character to the first name and set started flag to True
        first_name += char
        started = True

# Print the extracted first name
print("First name:", first_name)

#--------------------------------------
#-----------output---------------------
'''Enter your full name: sanjay sahu khetwani
First name: sanjay'''
