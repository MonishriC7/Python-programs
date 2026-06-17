import random

def find_polydivisible_num(current_num="", used_digits=None):
    if used_digits is None:
        used_digits = set()
        
    # Base case: successfully built a 10-digit number
    if len(current_num) == 10:
        return current_num
    
    # Pool of all available digits (0-9)
    all_digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    # Shuffle the digits randomly to satisfy the "random generation" intent
    random.shuffle(all_digits)
    
    for digit in all_digits:
        # Check digit repetition requirement
        if digit not in used_digits:
            next_num_str = current_num + digit
            next_len = len(next_num_str)
            
            # Divisibility condition check: 
            # First N digits must be divisible by N
            if int(next_num_str) % next_len == 0:
                used_digits.add(digit)
                
                # Recursively move to the next digit
                result = find_polydivisible_num(next_num_str, used_digits)
                if result:
                    return result
                
                # Backtrack if the path fails later
                used_digits.remove(digit)
                
    return None

if __name__ == "__main__":
    result = find_polydivisible_num()
    print("Generated 10-digit number:", result)
