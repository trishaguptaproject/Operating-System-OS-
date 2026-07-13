#3a. Write a python code for creating a variable and storing the text that we want to search
#Step 1: Ask the user to enter the text
text_to_search = input("Enter the text: ")

#Step 2: Ask the user to enter the word they want to search for
search_word = input("Enter the word to search for: ")

#Step 3: Search for the word in the text
if search_word in text_to_search:
    print(f"The word '{search_word}' was found in the text.")

else:
    print(f"The word '{search_word}' was NOT found in the text.")
