import pytest
from src.main import roman_to_int, int_to_roman, evaluate_expression


# Test function for roman_to_int()
def test_roman_to_int():
    
    # Test for a valid Roman numeral "X" which equals 10
    assert roman_to_int("X") == 10
    
    # Test for Roman numeral "IX", which is a subtractive form and equals 9
    assert roman_to_int("IX") == 9
    
    # Test for another subtractive form "IV", which equals 4
    assert roman_to_int("IV") == 4
    
    # Test for a more complex Roman numeral "MMXVIII", which equals 2018
    assert roman_to_int("MMXVIII") == 2018
    
    # Test for an invalid Roman numeral input, expecting a return of -1 or an error indicator
    assert roman_to_int("INVALID") == -1



# Test function for int_to_roman()
def test_int_to_roman():
    
    # Test for converting integer 25 to its Roman numeral equivalent "XXV"
    assert int_to_roman(25) == "XXV"
    
    # Test for converting the maximum Roman numeral value 3999, which should return "MMMCMXCIX"
    assert int_to_roman(3999) == "MMMCMXCIX"
    
    # Test for an invalid case of converting 0, as zero does not exist in Roman numerals
    assert int_to_roman(0) == "0 does not exist in Roman numerals."
    
    # Test for an out-of-bounds case, such as 4000, as Roman numerals don't typically represent this value
    assert int_to_roman(4000) == "You're going to need a bigger calculator."



# Test function for evaluate_expression()
def test_evaluate_expression():
   
    # Test for evaluating a valid arithmetic expression in Roman numerals "(V + X) * II" which should return "XXX"
    assert evaluate_expression("(V + X) * II") == "XXX"
    
    # Test for dividing Roman numerals, ex: "V / II" which equals "II"
    assert evaluate_expression("V / II") == "II"
    
    # Test for invalid expression input, expecting an error message indicating inability to parse
    assert evaluate_expression("INVALID") == "I don't know how to read this."
