import os

with open("myFile.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some random text\nMore random text\nAnd some more\n")

with open("myFile.txt", encoding="utf-8") as myFile:
    print(myFile.read())
os.rename("myFile.txt", "myFile2.txt")

with open("myFile2.txt", mode="r", encoding="utf-8") as file:
    lineNumber = 1
    word_count = 0
    character_count = 0
    
    # Read each line - readline()/loop
    # Count number of words in the list - loop
    # Count numner of characters in each word - loop
    for line in file:
        print("Line: {} {}".format(lineNumber, line), end="")
        words = line.split()
        word_count += len(words)
        for word in words:
            for character in word:
                character_count += 1
        lineNumber += 1
    
    print("Word count: {}".format(word_count))
    print("Character count: {}".format(character_count))
