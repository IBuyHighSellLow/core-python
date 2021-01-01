#! python3

# phoneAndEmail.py - finds phone number and email addresses on the clipboard

import pyperclip, re

phoneRegex = re.compile(r'^\d{3}-\d{3}-\d{4}$')

emailRegex = re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')


text= str(pyperclip.paste())

matches= []

for groups in phoneRegex.findall(text):
    phoneNum='-'.join([groups[1], groups[2], groups[5]])

    if groups[8] !='':
        phoneNum += ' x' + groups[8]
        matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

print(matches)

#copy results to clipboard

if len(matches) > 0 :
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No one numbers or email found')