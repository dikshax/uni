import time
import csv

def intro():
    welcome = 'Welcome to Traingle!'
    print(welcome.center(50))
    time.sleep(2)
    print('You are in a 40 meters deep dried up well.')
    time.sleep(2)
    print('There is no way that you could climb your way out.')
    time.sleep(2)
    print('But, there are three doors numbered 1, 2, 3.')
    time.sleep(2)
    print('One of the doors might be your way of here!')
    time.sleep(2)

def mode_game():
    print('Would you like to regiter or play as a guest?')
    mode = input('regester (r) or guest (g): ')
    return mode

def get_info():
    name = input('Please enter your name: \n')
    email = input('Please enter your E-mail: \n')
    return name, email

def choose_tunnel():
    print('Please enter the number of tunnel you want to enter.')
    choice = input('1, 2, or 3: ')
    return choice


def tunnel_one():
    print('You are infront of door number 1.')
    time.sleep(1)
    print('The door is locked, there is a 2 drawer cabinet build into the wall.')
    time.sleep(1)
    print('The key to the door is in the bottom draw and it\'s lucked.')
    time.sleep(1)
    print('Top draw is open!!')
    time.sleep(1)
    command = input('what you want to do: ')

    while command.lower() != 'remove draw':
        print(f'I don\'t understand \'{command}\'!')
        command = input('Try again!: ')

    if command.lower() == 'remove draw':
        print('You have removed the top draw and can see the key in\nbottom draw.')

    command = input('what you want to do: ')

    while command.lower() != 'pick key':
        print(f'I don\'t understand \'{command}\'!')
        command = input('Try again!: ')
    
    if command.lower() == 'pick key':
        print('You got the key now.')
        time.sleep(1)
        print('Opening the door ....')
        time.sleep(2)
        print('You enter a long tunnel. Walking along when you reach a\nsection with very deep dich filled with water.')
        command = input('what you want to do: ')

        while command.lower() != 'swim':
            print(f'I don\'t understand, {command}')
            command = input('What you want to do: ')

        if command.lower() == 'swim':
            print('You are swimming ..')
            time.sleep(2)
            print('You get to the other end and only see wall!')
            print('It\'s a dead end for you!')
        command = input('What you want to do: ')
        while command.lower() != 'get out':
            print(f'I don\'t get {command}!')
            command = input('Try again!: ')
        if  command.lower() == 'get out':
            print('You are back where you started!')

    

def tunnel_two():
    print('You are standing in fron of door number 2.')
    print('The door is locked and you hear a faint voice ..')
    print('In order to get access to the tunnel you most answer this question!!')
    answer = input('What is the magic word? ')
    while answer.lower() != 'abracadabra':
        print(f'{answer}, that is not the answer!')
        answer = input('Try again! ')
    if answer == 'abracadabra':
        print('You enter the tunnel, it\'s dark and gloomy inside.')
        print('Water is dripping from curved ceiling, there is lots of\ndebris laying on the floor and blocking your vision to see\nany further than 3 feet.')
        print('walking ...')
        time.sleep(2)
        print('You get at the end and it\'s a dead end. There is a table\nand there is a taser on the table.')

        command = input('what you want to do: ')
        while command.lower() != 'pick taser':
            print(f'I don\'t understand {command}!')
            command = input('Try again: ')
        if command.lower() == 'pick taser':
            print('You got the taser!')
            command = input('what you want to do now: ')

            while command.lower() != 'go back':
                print(f'I don\'t understant {command}')
                command = input('Try again, what you want to do: ')
            if command.lower() == 'go back':
                print('while you were walking back, you come face to face with a gaint rat.')
                print('The rat jumps high and bite your face. Your are\nbleading from your face!')
                command = input('what you want to do: ')

                while command.lower() != 'taser the rat':
                    print(f'I don\'t understand {command}!')
                    command = input('what you want to do: ')
                if command.lower() == 'taser the rat':
                    print('50 volts of electricity goes through rat\'s body and kills it immediately!')
                    print('You are walking out ...')
                    time.sleep(2)
                    print('You are back where you are started!')

def tunnel_three():
    print('You have standing by door number three')
    print('But you have to answer this riddle to in order to enter the tunnel.')
    time.sleep(2)
    print('The more of this there is, the less you see. What is it?')
    answer = input('Enter your answer: ')
    while answer.lower() != 'darkness':
        print(f'{answer}, that is wrong, try again!')
        answer = input('Enter your answer: ')
    if answer.lower() == 'darkness':
        print('You enter the tunnel and it\'s completely dark inside.')
        print('There is a log on the side, there a candle and light on the log.')
        command = input('what you want to do: ')
        while command.lower() != 'pick candle and light':
            print(f'I don\'t understand, {command}')
            command = input('what you want to do: ')
        if command.lower() == 'pick candle and light':
            print('You go the candle and light!')
        command = input('what you want to do: ')
        while command.lower() != 'light candle':
            print(f'I don\'t understand {command}')
            command = input('what you want to do: ')
        if command.lower() == 'light candle':
            print('The candle is on!')
            print('There tunnel is still dark and you only able to see like 2 meters.')
        command = input('what you want to do: ')
        while command.lower() != 'walk':
            print(f'I don\'t understand {command}')
            command = input('what you want to do: ')
        if command.lower() == 'walk':
            print('You are walking ... ')
            time.sleep(3)
            print('You approaching the end of the tunnle.')
            print('You can see the light ray coming through the key hole in the door.')
            time.sleep(2)
            print('You reach the door and can see the handle!')
        command = input('what you want to do: ')
        while command.lower() != 'open door':
            print(f'I don\'t understant {command}')
            print('Try again!!')
            command = input('what you want to do: ')
        if command.lower() == 'open door':
            print('You are out of the tunnel')
            print('congratulation!')