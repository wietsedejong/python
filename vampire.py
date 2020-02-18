# This program says hello and asks for my name
print('Hello World')
print('What is your name?')
myName = input()
print(' Its good to meet you, ' +myName)
print ('The lenght of you name is:')
print (len(myName))
print ('What is your age?')
myAge = int(input())
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
if myName == 'Alice':
    print('Hi, Alice.')
elif myAge < 12:
    print('You are not Alice, kiddo.')
elif myAge > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif myAge > 100:
    print('You are not Alice, grannie.')
