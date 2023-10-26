
# emailAndPhone.py - Finds phone numbers and email addresses on the clipboard.
#https://nostarch.com/contactus/
from pyperclip import *
from re import *

def phoneEmailSearch():
    phoneRegex = compile(r'''(
        (\d{3}|\(\d{3}\))?                # area code
        (\s|-|\.)?                        # separator
        (\d{3})                           # first 3 digits
        (\s|-|\.)                         # separator
        (\d{4})                           # last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
        )''', VERBOSE)

    # Create email regex.
    emailRegex = compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})       # dot-something
    )''', VERBOSE)

    # Find matches in clipboard text.
    text = str(paste())

    matches = []
    for groups in phoneRegex.findall(text):
        phoneNum = '-'.join([groups[1], groups[3], groups[5]])
        if groups[8] != '':
            phoneNum += ' x' + groups[8]
        matches.append(phoneNum)
    for groups in emailRegex.findall(text):
        matches.append(groups[0])

    # Copy results to the clipboard.
    if len(matches) > 0:
        # copy('\n'.join(matches))
        return '\n'.join(matches)
    else:
        return('No phone numbers or email addresses found.')\
            
print(phoneEmailSearch())
copy(phoneEmailSearch())