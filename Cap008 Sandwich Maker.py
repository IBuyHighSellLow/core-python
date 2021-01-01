import pyinputplus as pyip

print('Would you like to get a sandwich?')

answerSandwich = pyip.inputYesNo()

price= {
    'bread':{'weath': 4, 'white':5, 'sourdough':6},
    'protein':{'chicken':3, 'turkey':2, 'ham':4},
    'cheese': {'cheddar':1, 'mozzarella':1,'gouda':1},
    'topping':{'mayo':1, 'lettuce':1,'tomato':1}
}

totalPrice=0

if answerSandwich == 'yes':
    sandwichType = pyip.inputMenu(['weath','white','sourdough'], lettered=True, prompt='Please select what type of bread you want: \n')

    breadprice = price['bread'][sandwichType]
    totalPrice = breadprice

    proteinType = pyip.inputMenu(['chicken', 'turkey', 'ham'], lettered=True, prompt='What protein do you want? \n')

    totalPrice += price['protein'][proteinType]

    print('Do you want Cheese?')
    wantCheese = pyip.inputYesNo()
    if wantCheese== 'yes':
        cheeseType = pyip.inputMenu(['cheddar','parmesan','gouda'], numbered=True, prompt='What cheese would you want? \n')
        totalPrice += price['cheese'][cheeseType]
    else:
        print('No cheese selected.')
    
    print('Do you want an extra ingredient?')
    extraIngredient= pyip.inputYesNo()
    if extraIngredient == 'yes':
        extra = pyip.inputMenu(['mayo', 'lettuce', 'tomato'], numbered=True)
        totalPrice +=price['topping'][extra]
    else:
        print('No topping added.')
    

    print('How many sandwiches do you want?')
    qty= pyip.inputNum(greaterThan=0)
    totalPrice = totalPrice * qty

else:
    print('Have a nice day.')
print('Enjoy your ' + str(qty) + ' ' + str(sandwichType) + ' sandwiches, for a total of '+ str(totalPrice))    