from re import *
text = "this is a phone number at +1(503)-718-1287"
regComp = compile(
    r'''(\+\d)?(\d{3}|\(\d{3}\))?(\s|-|\.)?(\d{3})(\s|-|\.)?(\d{4})''')
matches = regComp.search(text)
print(matches.group(0))
