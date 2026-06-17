import random

def generate_polydivisible(current_num="", used_digits=None):
    if used_digits is None:
        used_digits = set()
        
    # Base Case: Successfully built a valid 10-digit number
    if len(current_num) == 10:
        return current_num
        
    # Available digits pool (0 to 9)
    digit_pool = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    # Shuffle the pool to ensure a randomized generation path
    random.shuffle(digit_pool)
    
    for digit in digit_pool:
        if digit not in used_digits:
            next_num_str = current_num + digit
            next_len = len(next_num_str)
            
            # Divisibility condition check: First N digits must be divisible by N
            if int(next_num_str) % next_len == 0:
                used_digits.add(digit)
                
                # Recursively move to the next position
                result = generate_polydivisible(next_num_str, used_digits)
                if result:
                    return result
                
                # Backtrack if this random branch runs into a dead end
                used_digits.remove(digit)
                
    return None

if __name__ == "__main__":
    unique_pattern_num = generate_polydivisible()
    print("Generated 10-digit number:", unique_pattern_num)
