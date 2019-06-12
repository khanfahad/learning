def swap_case(s):
    x = ""
    for char in s:
        if char.islower():
            x = x + char.upper()
        elif char.isupper():
            x = x + char.lower()
        else:
            x = x + char
    return x

s = input()
result = swap_case(s)
print(result)
