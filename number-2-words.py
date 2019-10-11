# Checking if user input is a valid number

Num = input("Type a POSITIVE number please: ")
while not(Num.isdigit()):
    print(F" Please make sure {Num} is a positive Number")  
    print("Please try again: ")
    Num = input()

# Dictionries

unitdigits = {'0': '', '1': 'One ', '2': 'Two ', '3': 'Three ', '4': 'Four ', '5': 'Five ', '6': 'Six ', '7': 'Seven ', '8': 'Eight ', '9': 'Nine '}
tens = {'0': 'Ten ', '1': 'Eleven ', '2': 'Twelve ', '3': 'Thirteen ', '4':'Forteen ', '5': 'Fifteen ', '6': 'Sixsteen ', 
         '7': 'Seventeen ', '8': 'Eighteen ', '9': 'Nineteen ' }
dozens = {'0': '', '2': 'Twenty ', '3': 'Thirty ', '4': 'Forty ', '5': 'Fifty ', '6': 'Sixty ', '7': 'Seventy ', '8': 'Eighty ', '9 ': 'Ninety '}
hundreds = {'0': '', '1': 'one Hundred ', '2': 'Two Hundred ', '3': 'Three Hunderd ', '4': 'Four Hundred ', '5': 'Five Hundred ',
            '6': 'Six Hundred ', '7': 'seven Hundred ', '8': 'Eight Hundred ', '9': 'Nine Hundred '}

comma_English = {'3': 'thousand, ', '6': 'million, ', '9': 'billion, '}

English = ''
Num_side = Num
num_length = len(Num)
Num_change = len(Num)
change = 3
while Num_change > 0:
    if Num == 0:
       English = 'zero'
       break

# Checking if the user input contains less than 2 digits

    if Num_side[Num_change -2] == '1':
       for digit in tens:
           if Num_side[Num_change - 1] == digit:
               English = tens[digit] + English
    else:
        for digit_1 in unitdigits:
            if Num_side[Num_change - 1] == digit_1:
                English = unitdigits[digit_1] + English
        if Num_change > 1:
            for digit_2 in dozens:
                if Num_side[Num_change -2] == digit_2:
                    English = dozens[digit_2] + English
    if Num_change > 2:
        for digit_3 in hundreds:
            if Num_side[Num_change - 3] == digit_3:
                English = hundreds[digit_3] + English
    if Num_change > 3:
        English = comma_English[str(change)] + English
    change = change + 3
    Num_change = Num_change - 3
print(English)
