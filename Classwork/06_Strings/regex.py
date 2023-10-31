from re import *

text = "this is a phone number at +1(503)-718-1287, i can also be reached at 971-221-1283 or (942).357.4318"
regComp = compile(
    r'''(\+(?:\d)*)?(\d{3}|\(\d{3}\))?(\s|-|\.)?(\d{3})(\s|-|\.)?(\d{4})''')
matches = regComp.findall(text)
print(matches)
