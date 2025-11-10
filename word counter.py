#word counter program

text=input("Enter a sentence or paragraph:\n")
words=text.split()
word_count=len(words)
print(f"The number of words in given text is: {word_count}")
