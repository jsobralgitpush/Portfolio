import cs50
import sys

#Asking for user input
user_input = cs50.get_string("Text: ")

#Number of words
list_words = user_input.split(" ")
num_words = len(list_words)

#Number of letters
num_letters = 0
for i in range(num_words):
    for j in range(len(list_words[i])):
        if str.isalpha(list_words[i][j]) == True:
            num_letters +=1  

#Number of sentence
num_sentences = 0
for i in user_input:
    if i in [".","!","?"]:
        num_sentences+=1

#Calculating the "L" and the "S"
x = 100/num_words
L = x*num_letters
S = x*num_sentences

#Calculate the grade
coleman_liau_exp = 0.0588 * L - 0.296 * S - 15.8

#Checking the border conditions
if round(coleman_liau_exp) < 1:
    print("Before Grade 1")
    exit(0)
elif round(coleman_liau_exp) > 16:
    print("Grade 16+")
    exit(0)

print(f"Grade {round(coleman_liau_exp)}")
#print("Letters: {} | Words: {} | Sentences: {}".format(num_letters,num_words,num_sentences))