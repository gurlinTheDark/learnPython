sentence = "Hi there Archana here"
vowels = ["a","e","i","o","u"]

list = sentence.split(' ')
max_vowel_count = 0
max_vowel_string = ""
def count_vowels(w):
    count_vowel = 0
    for vowel in vowels:
        count_vowel = count_vowel + w.count(vowel)
    return count_vowel
    
for word in list:
    count = count_vowels(word.lower())
    print(count)
    if count > max_vowel_count:
        max_vowel_string = word
        max_vowel_count = count
print("Max vowels in", max_vowel_string)
