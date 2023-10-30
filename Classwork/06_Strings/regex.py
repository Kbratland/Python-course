from re import *
text = "this is a phone number at (503)-718-1287"
regComp = compile(r'''\d{3}-\d{3}-\d{4} | \(\d{3}\)-\d{3}-\d{4}''')
match = regComp.search(text)
print(match.group())