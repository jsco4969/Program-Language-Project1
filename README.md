# Program Language Project1
Description: <br>
For this project, you must create a calculator that works in Roman numerals. Your application should take
an equation as command line parameters and print the resulting number in roman numerals. For
example, this could be how I call your application and what I’d expect the result to be:
<br>

Python main.py (VII + V ) * II + I
XXV

<br>

Roman numerals do not have concepts of floating-point numbers, negative numbers, or zero. As a result,
the user, me, will not try to input any of these. Similarly, you should not report any of these either:

- If the result of an operation would result in zero, your application should print: “0 does not exist
in Roman numerals.”
- If the result of an operation would result in a floating-point number, your application should
print: “There is no concept of a fractional number in Roman numerals.”
- If the result of an operation would result in a negative number, your application should print:
“Negative numbers can’t be represented in Roman numerals.”
- If the result of an operation would result in a number greater than 3,999, your application
should print: “You’re going to need a bigger calculator.”
- If the input cannot be parsed, your application should print: “I don’t know how to read this.”
<br>

Additional project details are as follows:<br>
- Entry of a number into your application without any operations or other numbers should simply
print the number as their English numeral representation, i.e. VI should print 6.
- Only 4 operations must be supported: addition, subtraction, multiplication, and division.
- The order of operations matters. Multiplication and division should occur before multiplication
and subtraction.
- Two grouping operators may be used in the program input: ( ) and [ ]. Grouping operators take
precedence over multiplication and division.

## documentation
```
def roman_to_int(roman)
```
- what it does:<br> Convert a Roman numeral string to an integer.
- Arg: <br> ``roman (str)``: Roman numeral string.
- Return: <br> int: The equivalent integer, or -1 for invalid input.
```
def int_to_roman(number)
```
- what it does: <br> Convert an integer to a Roman numeral string.
- Arg: <br> ``number (int)``: Integer to convert.
- Return: <br> str: Roman numeral string, or error message if invalid.
```
def evaluate_expression(expression)
```
- what it does: <br> Evaluate a Roman numeral arithmetic expression.
- Arg: <br> ``expression (str)``: Arithmetic expression using Roman numerals.
- Return: str: <br> Resulting Roman numeral or error message.

```
  roman_to_int(roman)
```
- what it does: <br> Converts a Roman numeral string to its corresponding integer value. The function handles both additive and subtractive Roman numeral notations.
- Arg: <br> ``roman (str)``: A string representing a Roman numeral 
- Return: str: <br> ``int``: The integer representation of the Roman numeral. Returns ``-1`` if the input is invalid.
```
  int_to_roman(number)
```
- what it does: <br> Converts an integer into its Roman numeral equivalent.
- Arg: <br>`` number (int)``: An integer to be converted into Roman numerals. Valid range is from 1 to 3999.
- Return: str: <br> ``str``: A string representing the Roman numeral equivalent of the integer. If the integer is 0 or out of range (> 3999), a corresponding error message is returned.
```
  evaluate_expression(expression)
```
- what it does: <br> Evaluates an arithmetic expression written using Roman numerals.(* - / +)
- Arg: <br> ``expression (str)``: A mathematical expression involving Roman numerals and arithmetic operators ex: ("(V + X) * II").
- Return: str: <br> ``str``: The result of the expression as a Roman numeral string. If an error occurs, an appropriate error message is returned.
