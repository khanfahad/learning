import textwrap

def wrap(string, max_width):
    newString = ""
    for char in range(0, len(string), max_width):
        newString += string[char:char+max_width]
        newString += "\n"
    return newString

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)
