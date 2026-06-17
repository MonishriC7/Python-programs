num = int(input("Input: "))

for step in range(1, 6):
    # Convert number to string to easily reverse it
    num_str = str(num)
    rev_str = num_str[::-1]
    
    # Calculate the sum of the number and its reverse
    total = num + int(rev_str)
    print(f"Step {step}: {num} + {rev_str} = {total}")
    
    # Check if the total is a palindrome
    total_str = str(total)
    if total_str == total_str[::-1]:
        print("Output: It is a palindrome")
        break
    
    # If not a palindrome, set total as the next input
    num = total
else:
    # This runs only if the loop finishes 5 steps without a break
    print("Output: Palindrome not obtained in 5 steps")
