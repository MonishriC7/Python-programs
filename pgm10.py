text = input("Input: ")
chars = list(text)

# Extract and reverse only the alphanumeric letters
alpha_reversed = [c for c in chars if c.isalnum()][::-1]

# Rebuild the list: insert reversed letters back into alphanumeric spots
idx = 0
for i in range(len(chars)):
    if chars[i].isalnum():
        chars[i] = alpha_reversed[idx]
        idx += 1

print("Output:", "".join(chars))
