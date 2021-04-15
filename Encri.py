from cryptography.fernet import Fernet


print(' _____                       ')
print('| ____|_ __   ___ _ __ _   _ ')
print("|  _| | '_ \ / __| '__| | | |")
print('| |___| | | | (__| |  | |_| |')
print('|_____|_| |_|\___|_|   \__, |')
print('                       |___/ ')


#Encrypth e Decrypth
def encrip(nome, key, times):
	#Ler 
	for i in range(times):
		with open(nome, "rb") as file:
			data = file.read()
    	#Encriptar
		encry = f.encrypt(data)
    	#Escrever
		with open(nome, "wb") as file:
			file.write(encry)
		
		percent = (i / times)*100
		print('[+]'+str(percent)+'%'+'\r', end='')

def decri(nome, key, times):
	for i in range(times):
		#Ler
		with open(nome, "rb") as file:
			data = file.read()
    	#Decriptar
		decry = f.decrypt(data)
    	#Escrever
		with open(nome, "wb") as file:
			file.write(decry)

		percent = (i / times)*100
		print('[+]'+str(percent)+'%'+'\r', end='')

#Chave
Need = input('Need a new Fernet Key?(Y/N)\n')
if Need.lower() == 'y':
	print('\n\n-----------------------------------------')
	print("Keep this key really safe!!!")
	print(str(Fernet.generate_key())[2:-1])
	print('\nWARNING\n\nYou can only Decrypt Files if the got \nencrypted it the same Fernet Key\n')
	print('-----------------------------------------\n\n')


Key = input('Input Fernet key!\nKey = ')
f = Fernet(Key)
Sair = True
#Encriptar Ou Decriptar
while Sair:

	Res = input('1- Encript\n2- Decript\n3-Exit\n')
	if Res == '1':
		nome = input('Name File?\n')
		times = int(input('Times to encrypt (the more encrypted, more the space!)\n'))
		encrip(nome, Key, times)
	elif Res == '2':
		nome = input('Name File?\n')
		times = int(input('Times to decrypt (Decrypt the same times you Encrypted)\n'))
		decri(nome, Key, times)
	elif Res == '3': 
		Sair = False


