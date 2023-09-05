#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        TypeError("text must be a string")
    new_text = ""
    for index in range(len(text)):
        if text[index] in ".?:":
            new_text += "\n\n"
        else:
            new_text += text[index]
    return new_text