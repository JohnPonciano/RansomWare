import os
import binascii

import pyaes


file_name = "foto.jpg"
file = open(file_name, 'rb')
file_data = file.read()
file.close()

#sistema operacional remove o arquivo
#os.remove(file_name)

#lembrar de criar um algoritimo para proteção da chave.
key = "0123456789abcdef"
aes = pyaes.AESModeOfOperationCTR(key)
crypto_data = aes.encrypt(file_data)
crypto_data_hex = binascii.hexlify(crypto_data)


#save file
new_file_name = file_name + ".natalia"
new_file = open(new_file_name, 'wb')
new_file.write(crypto_data)
new_file.close()
