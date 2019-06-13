def solve(s):
    capitalizedName = ""
    if len(s) > 0 and len(s) < 1000:
        capitalizedName = ' '.join(map(str.capitalize, s.split(' ')))
        return capitalizedName

s = input()

result = solve(s)
print(result)
