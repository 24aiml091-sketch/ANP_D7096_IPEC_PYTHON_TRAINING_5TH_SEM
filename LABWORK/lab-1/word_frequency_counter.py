'''Problem Statement: 
Accept a sentence from the user and create a dictionary that stores the frequency of each word.
 Example: 
Input: python is easy and python is powerful 
Output:
 { 
 'python': 2, 
 'is': 2, 
 'easy': 1, 
 'and': 1, 
 'powerful': 1 } '''

#----------------------------------coding------------------------------
# Input the sentence from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words (case-insensitive)
words = sentence.lower().split()

# Create a dictionary to store the frequency of each word
my_dict = {}

for word in words:
    # Remove punctuation marks 
    cleaned_word = word.strip(".,!?;:()[]\"'")
    if cleaned_word:
        # Increment frequency if it's already in the dictionary
        if cleaned_word in my_dict:
            my_dict[cleaned_word] += 1
        else:
            my_dict[cleaned_word] = 1

# Print the resulting dictionary
print(my_dict)
