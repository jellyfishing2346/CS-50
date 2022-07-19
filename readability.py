# Prompt the user to enter a string for text
from cs50 import get_string
textPrompter = get_string("Text: ")
# Set the words, letters, and sentences to 0
numLetters = numWords = numSentences = 0
# Test the character conditions for words, letters, and sentences
for character in textPrompter:
    if character.isalpha():
        numLetters += 1
    if character.isspace():
        numWords += 1
    if character in ['?', '.', '!']:
        numSentences += 1
# Increment the number of words
numWords += 1
# The formulas for letters and sentences
L = (numLetters * 100.0) / numWords
S = (numSentences * 100.0) / numWords
finalResult = int((0.0588 * L - 0.296 * S - 15.8) + 0.5)
# Determine the following conditions to determine the text's grade level
if finalResult < 1:
    print("Before Grade 1")
elif finalResult >= 16:
    print("Grade 16+")
else:
    print("Grade {finalResult}")

