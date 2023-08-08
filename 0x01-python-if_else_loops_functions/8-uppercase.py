def uppercase(str):
    for letter in str:
        print(chr(ord(letter) - 32), end="")
    print()
