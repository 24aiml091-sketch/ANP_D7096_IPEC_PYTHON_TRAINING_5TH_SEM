'''Write a Python program that defines a function count_vowels(text). 
The function should:
 • Accept a string.
  • Count the total number of vowels (a, e, i, o, u) irrespective of case. 
   • Return the total vowel count.
   
      The main program should:
    • Accept a sentence from the user. 
     • Call the function. 
      • Display the total number of vowels.'''
#--------------------------------------------------
def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"
    for char in text:
        if char in vowels:
            count += 1
    return count

#------------------------------------------------------------------------
sentence = input("Enter the sentence :")
print("Total number of vowels :",count_vowels(sentence))

#---------------------------output-----------------------
'''Enter the sentence :hello world
Total number of vowels : 3'''
