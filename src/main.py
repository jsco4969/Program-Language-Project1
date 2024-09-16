import re

# Roman numeral to integer mapping
# Maps each Roman numeral character to its corresponding integer value.
roman_to_int_map = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
}

# Integer to Roman numeral mapping
# Defines a list of tuples, each mapping an integer value to its Roman numeral counterpart.
int_to_roman_map = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
    (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'),
    (4, 'IV'), (1, 'I')
]



# Convert a Roman numeral string to an integer.
def roman_to_int(roman):
    
    total = 0  # Holds the total integer value.
    prev_value = 0  # Tracks the value of the previous numeral to handle subtraction.
    
    # Loop through the Roman numeral string in reverse order.
    for numeral in reversed(roman):
        value = roman_to_int_map.get(numeral)  # Get the integer value of the current numeral.
        
        # Return -1 if the numeral is invalid.
        if value is None:
            return -1  # Invalid Roman numeral
        
        # If the current value is smaller than the previous one, subtract it (for cases like IV, IX).
        if value < prev_value:
            total -= value
        else:
            total += value  # Otherwise, add it to the total.
        
        prev_value = value  # Update the previous numeral value.
    
    return total  # Return the final total as the converted integer.



# Convert an integer to a Roman numeral string.
def int_to_roman(number):
    
    # Roman numerals do not represent numbers less than 1.
    if number < 1:
        return "0 does not exist in Roman numerals."
    
    # Roman numerals typically do not represent numbers greater than 3999.
    if number > 3999:
        return "You're going to need a bigger calculator."
    
    roman = ""  # Holds the resulting Roman numeral string.
    
    # Iterate over the mapping from large to small values.
    for value, numeral in int_to_roman_map:
        # Append the corresponding numeral to the result while the number is greater than or equal to the value.
        while number >= value:
            roman += numeral
            number -= value  # Subtract the value from the number.
    
    return roman  # Return the final Roman numeral string.



# Evaluate a Roman numeral arithmetic expression.
def evaluate_expression(expression):
    
    try:
        # Remove spaces from the expression to clean up input.
        expression = expression.replace(" ", "")
        
        # Split the expression into individual tokens (numbers and operators) using regex.
        parsed_expression = re.split(r'([+\-*/()])', expression)
        
        # Convert Roman numerals to integers in the parsed expression.
        parsed_expression = [roman_to_int(token) if token not in '+-*/()' else token for token in parsed_expression]

        # Check if the expression contains any invalid Roman numerals.
        if -1 in parsed_expression:
            return "I don't know how to read this."
        
        # Use the eval function to compute the result of the arithmetic expression.
        result = eval("".join(map(str, parsed_expression)))

        # Handle various edge cases for the result.
        if result < 0:
            return "Negative numbers can't be represented in Roman numerals."
        if result == 0:
            return "0 does not exist in Roman numerals."
        if isinstance(result, float):
            return "There is no concept of a fractional number in Roman numerals."
        if result > 3999:
            return "You're going to need a bigger calculator."
        
        # Convert the resulting integer back to a Roman numeral and return it.
        return int_to_roman(int(result))

    except Exception:
        # If any error occurs during parsing or evaluation, return an error message.
        return "I don't know how to read this."



# Main 
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        # If no expression is provided, prompt the user to input one.
        print("Please provide a mathematical expression.")
    else:
        # Join the command-line arguments into a single string as the expression.
        input_expression = " ".join(sys.argv[1:])
        # Evaluate the expression and print the result.
        print(evaluate_expression(input_expression))
