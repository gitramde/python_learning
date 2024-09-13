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
            b. If at least one of encoding or errors is given, object should be bytes-like object (bytes or bytearray)
                i. More details when learning about the bytes and bytearray

    NOTE - Learn more about the string literals here https://docs.python.org/3.11/reference/lexical_analysis.html#strings
"""

"""
    String Formatting (4 different formatting options) 
        1. printf-style
            a. Uses String Formatting or Interpolation operator (% Operator (modulo))
            b. format % values --> format is the string and values can be a single non-tuple object or tuple with exact 
               number of items specified in the format string. 
        2. formatted string strings (f string)
        3. str.format()
        4. template_strings 
    
"""


