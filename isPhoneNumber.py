message = 'a distinct section of a piece of writing, usually dealing with a 415-555-1012 single theme and indicated by a new line, indentation, or numbering.a distinct 415-555-1014 section of a piece of writing, usually dealing with a single theme and indicated by a new line, indentation, or numbering.'

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False

    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

isPhoneNumber(message)


for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')
