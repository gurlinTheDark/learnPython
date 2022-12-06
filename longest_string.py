string = "fly  me   to the moon"

longest = ""
split_string = string.split()
for i in range(len(split_string)):
    print("before space, %s, after space" %split_string[i])
    if len(split_string[i]) > len(longest):
        longest = split_string[i]
print("The word with maximum length is %s" % longest)
