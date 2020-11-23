import os
import binascii

import pyaes


file_name = "foto.jpg"
file = open(file_name, 'rb')
file_data = file.read()
file.close()


#lembrar de criar um algoritimo para proteção da chave.
key = "0123456789abcdef"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.encrypt(file_data)



#save file
new_file_name = file_name + ".natalia"
new_file = open(new_file_name, 'wb')
new_file.write(decrypt_data)
new_file.close()
