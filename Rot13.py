string = "ashwin"
chr_string = ""
for i in range(len(string)):
    if ord(string[i]) <= 109:
        new_ord = ord(string[i]) + 13
    if ord(string[i]) > 109:
        new_ord = ord(string[i]) - 13
    chr_string = chr_string + chr(new_ord)
print(chr_string)
