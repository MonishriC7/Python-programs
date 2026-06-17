import math

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
        
    # Check odd factors up to the square root of n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def next_prime(x):
    """Finds the smallest prime number strictly greater than x."""
    # Handle negative numbers, 0, and 1 directly
    if x < 2:
        return 2
        
    # Start checking from the next sequential integer
    candidate = int(x) + 1
    
    # Keep checking until a prime number is found
    while True:
        if is_prime(candidate):
            return candidate
        candidate += 1

# Example Usage
x_value = 20
print(f"The smallest prime greater than {x_value} is {next_prime(x_value)}")
# Output: The smallest prime greater than 20 is 23
