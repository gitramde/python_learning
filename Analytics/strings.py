"""
    Text Sequence Type -- str: (One of the built-in python types)
    https://docs.python.org/0.11/library/stdtypes.html#text-sequence-type-str
        1. Textual data in python is handled with str objects or strings.
        2. strings are immutable sequence (can't be modified once created)
        3. Define a string
            a. Single Quotes ('allows embedded "double" quotes')
            b. Double Quotes ("allows embedded 'single' quotes')
            c. Triple Single or Double Quotes (can span multiple lines and whitespaces included)
        4. Strings can also be created from other objects using the str constructor
        5. No separate character type. Indexing a string produces string of length 1 (s[0] == s[0:1])
        6. str(object = '') or str(object=b'', encoding='utf-8", errors='strict') - Returns string version of an object.
            a. If neither encoding nor errors is given
                i. str(object) returns printable string representation of the object [type(object).__str__(object)]
                ii. If object does not have __str__() method then str() falls back to returning repr(object) - a string
                    containing a printable representation of an object.
                iii. repr() meant to generate representations which can be read by the interpreter. For objects which
                    don’t have a particular representation for human consumption, str() will return the same value as repr()
            b. If at least one of encoding or errors is given, object should be bytes-like object (bytes or bytearray)
                i. More details when learning about the bytes and bytearray

    NOTE - Learn more about the string literals here https://docs.python.org/3.11/reference/lexical_analysis.html#strings
"""

"""
    String Formatting (4 different formatting options) 
        1. printf-style (
            a. Uses String Formatting or Interpolation operator (% - Modulo Operator)
            b. format-string % values --> * format-string is the string to be formatted;  
                                          * values can be a single non-tuple object or TUPLE with exact number of items 
                                          specified in the format string or a DICTIONARY that has a value for each key. 
            c. Conversion Specifier has to be in the below order 
                %[Mapping key][flags][width][.precision][length]type 
                i. Mapping key - parenthesised sequence of characters. example: (someone)
                ii. Conversion flags -     
                        '#' - value conversion will use alternate form. 
                        '0' - zero padding for numeric values 
                        '-' - converted value is left adjusted (overrides '0' conversion)
                        ' ' - blank space before a positive number
                        '+' or '-' - sign that precedes the conversion 
                iii. Conversion type ('d' & 'i' - signed integer decimal; 'o' - signed octal value, 
                                      'e' or 'E' floating point exponential lower & upper case, 
                                      'f' or 'F' floating point lower or upper case, 'c' - character, 
                                      'r' - string using repr(), 's' - string using str(), 'a' - string using ascii
                NOTE: width and length can display any number of characters above the specified value (minimum characters)
        2. formatted string strings (f string)
            a. Begin with a f or F
            b. Write a Python expression between { and } characters that can refer to variables or literal values.
        3. str.format()
        4. template_strings 
    
"""

# ----------------------- printf style examples ---------------------------- #

print('%(language)s has %(number)03d quote types.' %
      {'language': 'Python', "number": 2})
# output - Python has 002 quote types.
# uses mapping key, flag '0', length modifier and type; uses dictionary for values

print (" Grocery Cost : %5.2f;  Number of Items: %5d" % (258.456, 800))
#  Grocery Cost : 258.46;  Number of Items:   800
# %5.2f - String need to have minimum 5 digits and 2 decimal points. if not, left padded with spaces

# ----------------------- Formatted String Literals - f string ---------------------------- #




