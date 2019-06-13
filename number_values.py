x = int(input())
w = len(str(bin(x)).replace('0b',''))
for i in range(1, x+1):
    b = bin(int(i)).replace('0b','').rjust(w, ' ')
    o = oct(int(i)).replace('0o','', 1).rjust(w, ' ')
    h = hex(int(i)).replace('0x','').upper().rjust(w, ' ')
    j = str(i).rjust(w, ' ')
    print(j, o, h, b)
