n = int(input("Input: "))
out = ["0"]

for i in range(1, n + 1):
    # Create the sequence (e.g., '321')
    seq = "".join(str(j) for j in range(i, 0, -1))
    # Mirror it around '0' (e.g., '321' + '0' + '123')
    out.append(seq + "0" + seq[::-1])

print("Output:", " ".join(out))
