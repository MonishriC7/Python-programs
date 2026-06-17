word = input("Enter a word: ")
result = ""
for i in word:
    if i not in "aeiouAEIOU":
        result = result + i
print("Output:", result)
