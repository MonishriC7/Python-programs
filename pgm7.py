rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

total_sum = 0

for i in range(rows):
    for j in range(cols):
        num = int(input("Enter number: "))
        total_sum += num

print(total_sum)
