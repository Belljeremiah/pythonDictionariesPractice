"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions["boondoggle"] = "work or activity that is wasteful or pointless but gives the appearance of having value."
word_definitions ["verisimilitude"] = "the appearance of being true or real."
word_definitions ["torpid"] = "mentally or physically inactive; lethargic."
word_definitions ["turbid"] = "(of a liquid) cloudy, opaque, or thick with suspended matter."
word_definitions ["diadem"] = "a jeweled crown or headband worn as a symbol of sovereignty."

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
print(word_definitions["diadem"])
print(word_definitions["torpid"])


"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""
for (key, value) in word_definitions.items():
    print(f"The definition  of {key}: is {value}")

