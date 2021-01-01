import webbrowser, sys, pyperclip, pyinputplus

print('Fran, quieres ver tus paginas favoritas?. Presione 0 para cancelar')
x= pyinputplus.inputYesNo()

if x == 'yes':
    webbrowser.open('https://stocktwits.com/')
    webbrowser.open('https://google.com')
else:
    print('Gracias Fran')

    

