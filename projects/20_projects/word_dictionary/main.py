def main():
    word_dictinary = {
        "hi": "a way of greeting",
        "eyes": "an organ for seeing",
        "earth": "a planet in space"
    }
    
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        if word in word_dictionary:
            print(word,":", word_dictionary[word])
            
main()