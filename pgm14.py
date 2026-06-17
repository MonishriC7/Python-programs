def is_valid_brackets(s):
    # Dictionary to match closing brackets with opening brackets
    bracket_map = {")": "(", "}": "{", "]": "["}
    stack = []
    
    for char in s:
        # If it's a closing bracket
        if char in bracket_map:
            # Pop the top element if stack is not empty, else use a dummy value
            top_element = stack.pop() if stack else '#'
            
            # If the mapping doesn't match, it's invalid
            if bracket_map[char] != top_element:
                return "Not a valid string"
        else:
            # If it's an opening bracket, push it onto the stack
            stack.append(char)
            
    # If the stack is empty, all brackets matched perfectly
    return "Valid string" if not stack else "Not a valid string"

# Test the code
user_input = input("Input: ")
print("Output:", is_valid_brackets(user_input))
