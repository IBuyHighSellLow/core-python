import regex

phoneNumRegex = regex.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is gjhrgreg sdgfsag er eqtgeqrt et ewrt qert et q 435-545-4022     qetr qertq  435-545-4022.')
print('Phone number found: ' + mo.group())

