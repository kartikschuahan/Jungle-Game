##Jungle game
print('Welcome to the game')
while True:
    ask=int(input('Do you wanna play game press 1\nDo you want to exists press2\n'))
    if ask==1:
        name=input('Enter your name: ')
        print(f'Hi {name}, you get lost in a middle of jungle now you have to find way out')
        option=input('You have 2 option take Left or Right\n').lower().strip()
        if option == 'left':
            print('You fall in the pit')
        elif option == 'right':
            option=input('You have 2 option take Left or Right\n').lower().strip()
            if option == 'left':
                print('snakes bites you')
            elif option == 'right':
                option=input('You have 2 option take Help or Own way\n').lower().strip()
                if option == 'help':
                    print('You Win')
                elif option == 'own way':
                    print('You are very arrogant')
                else:
                    print('Please check the input')
            else:
                print('Please check the input')
        else:
            print('Please check the input')
    else:
        print('Thanks for visit')
        break
