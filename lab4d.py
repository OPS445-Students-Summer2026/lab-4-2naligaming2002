#!/usr/bin/env python3

def first_five(text):
    return str(text)[:5]

def last_seven(text):
    return str(text)[-7:]

def middle_number(number):
    text = str(number)

    if "." in text:
        dot = text.index(".")
        return text[dot:dot+2]
    else:
        middle = len(text) // 2
        return text[middle-1:middle+1]

def first_three_last_three(str1, str2):
    return str1[:3] + str2[-3:]

if __name__ == "__main__":
    pass
