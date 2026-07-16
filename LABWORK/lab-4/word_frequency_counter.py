'''Problem 9: Word Frequency Counter
 Topics: Function, Dictionary, String, List Accept a sentence from the user.
 Create a function:
 word_frequency(sentence) 
The function should: 
• Remove punctuation. 
 • Ignore case sensitivity.
  • Count frequency of every word.
  • Display words in alphabetical order. 
 • Print the most repeated word'''
#-------------------------------------------

#creating the function:
def word_frequency(sentence):

    sentence = sentence.lower()

    for ch in string.punctuation:
        sentence = sentence.replace(ch,"")

    words = sentence.split()

    freq = {}

    for word in words:
        freq[word] = freq.get(word,0)+1

    for word in sorted(freq):
        print(word,":",freq[word])

    most = max(freq,key=freq.get)

    print("Most Repeated:",most)
#print the sentence:
text = input("Enter Sentence: ")

word_frequency(text)
#----------------------------------------
#--------output--------------------------
'''Input:
Python is easy.
 Python is powerful. 
Output 
easy :1 
is :2 
powerful :1 
python :2 '''