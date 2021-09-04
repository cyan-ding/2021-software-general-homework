# Set the variable in_list to whatever value you want. Let's use 
# [ 5, 2, 3, 1, 4, 6, 8, 7 ] as an example.

# Use for loops, while loops, and whatever else we've learned to 
# set the variable x to the length of in_list - but you may NOT use len! 
# Try to mimic the behavior of len.
lst = [ 5, 2, 3, 1, 4, 6, 8, 7 ]
length = 0
for i in lst:
  length +=1 
print(length)

################################################
# Create a program to accept words from a user, and add them to a dictionary. 
# At the end, use print(mydict) to print out the user's work to them

word1 = input("Please enter a word, or press enter to end: ")
word2 = input("Please enter the word's translation: ")
dic = {word1: word2}
print(dic)


################################################
# Extend your dictionary program from assignment #2 to have some added capabilities:

# Make sure the user cannot enter more than one translation for the same word, 
# in either direction. For example, if ‘dog’: ‘Hund’ is already an entry in the 
# dictionary, then adding a new translation for ‘dog’ OR another word that translates 
# to ‘Hund’ should fail.

# Make sure the user cannot input a key that contains a space, but a value that 
# contains a space is acceptable. So adding ‘the dog’ : ‘Hund’ should fail, but 
# ‘dog’ : ‘der Hund’ is fine.
word3 = input("Please enter a word, or press enter to end: ")
word4 = input("Please enter the word's translation: ")


dic1 = {word3: word4}
word1 = word3
word2 = word4
if word3 in dic:
  print("Error: Failed")
elif word4 in dic:
  print("Error: Failed")
elif " " in word3:
  print("Fail")
else:
  sentence = input("Enter a sentence: ")
  sentence1 = sentence.split()
  string = ""
  if word3 in sentence1:
    for i in range(len(sentence1)):
      if sentence1[i] == word3:
        sentence1[i] = word4
    for i in range(len(sentence1)):
      if i == 0:
        string = string + sentence1[i]
      else:
        string = string + " " + sentence1[i]
    print(string)
  
  else:
    print(sentence)
  
  

################################################
# Instead of printing out the dictionary when the program is done, ask the user 
# for a sentence and “translate” it, word-by-word, as output. 

# If a word has no translation, use the word unchanged.
