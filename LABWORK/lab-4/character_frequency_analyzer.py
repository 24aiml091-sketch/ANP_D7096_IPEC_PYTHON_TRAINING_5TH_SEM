'''Problem 2: Character Frequency Analyzer-----------
 Accept a string from the user and perform the following:
 • Count uppercase letters  
• Count lowercase letters  
• Count digits  
• Count special characters  
• Print the most frequently occurring character  
Example:
 Input: Python@2026 
Output:
 Uppercase : 1 
Lowercase : 5 
Digits : 4 
Special Characters : 1
 Most Frequent Character : 2'''
#--------------------------------------------

#taking input string from user:
text = input("Enter a string: ")

upper = lower = digit = special = 0
freq = {}
#Checking the cases:
for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    else:
        special += 1

    freq[ch] = freq.get(ch, 0) + 1

most = max(freq, key=freq.get)
#print the cases as printout:
print("Uppercase:", upper)
print("Lowercase:", lower)
print("Digits:", digit)
print("Special Characters:", special)
print("Most Frequent Character:", most)

#--------------------------------------
#--------output----------------------
Input: Python@2026 
Output:
 Uppercase : 1 
Lowercase : 5 
Digits : 4 
Special Characters : 1
 Most Frequent Character : 2