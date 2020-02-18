
 while True:
	print('Who are you?')
	name = input()
	if name != 'Joe':
		continue
	print ('Hallo , joe wat is het wachtwoord? (het is iets met een vis)')
	password = input()
	if password == 'swordfish':
		break
print('Access grandted.')
