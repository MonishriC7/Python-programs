text = input("Input: ")
chars = list(text)

# Extract and reverse only the letters and numbers
alpha_reversed = [c for c in chars if c.isalnum()][::-1]

# Put the reversed characters back into the alphanumeric positions
idx = 0
for i in range(len(chars)):
    if chars[i].isalnum():
        chars[i] = alpha_reversed[idx]
        idx += 1

print("Output:", "".join(chars))
