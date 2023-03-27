# import libraries


# Get the input from the user
Text = input("Write the english message to translate into pig Latin:\n")

# Processing into pig latin
# Checking for the vowels
Vowels = ["a", "e", "i", "o", "u", "y"]

# getting the data into a list
AllTheWords = []

# Checking eacch word
for word in Text.split(" "):
    NonWords = ""
    # Checking for the non letters in the beginning of each word
    while len(word) > 0 and not word[0].isalpha():
        NonWords += word[0]
        word = word[1:]
    if len(word) == 0:
        AllTheWords.append(NonWords)
        continue

    # Checking the non letters in the end of each word
    NonSuffix = ''
    while len(word) > 0 and not word[-1].isalpha:
        NonSuffix += word[-1]
        word = word[:-1]

    # Remembering the upper and title case of the word
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower()  # Make the word lowercase for the transaction

    # Separate the consonants at the start of this word:
    prefixConsonants = ''

    while len(word) > 0 and not word[0] in Vowels:
        prefixConsonants += word[0]
        word = word[1:]
    
    # Add the Pig Latin ending to the word:
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'
    
    # Set the word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()
    
    # Add the non-letters back to the start or end of the word.
    AllTheWords.append(NonWords + word + NonSuffix)
    
# Join all the words back together into a single string:
print(' '.join(AllTheWords))
