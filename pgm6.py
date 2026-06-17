text = input("Enter a string: ")
result = ""
vowels = "aeiouAEIOU"

for i in range(len(text)):
    current_char = text[i]
    if current_char in vowels:
        has_left_vowel = (i > 0 and text[i - 1] in vowels)
        has_right_vowel = (i < len(text) - 1 and text[i + 1] in vowels)
        if has_left_vowel or has_right_vowel:
            result += current_char
    else:
        result += current_char

print(result)
