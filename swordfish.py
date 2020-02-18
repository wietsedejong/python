Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> while Ture:
	print('Who are you?')
	name = input()
	if name != 'Joe':
		continue
	print ('Hallo , joe wat is het wachtwoord? (het is iets met een vis)')
	password = input()
	if password == 'swordfish':
		break
	print('Access grandted.')