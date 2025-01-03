import os
import pyaes


file = open("text.txt.ransomwaretroll", "rb")
file_data = file.read()
file.close()

## chave para descriptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remover o arquivo criptografado
os.remove("text.txt.ransomwaretroll")

## criar o arquivo descriptografado
new_file = "text.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()