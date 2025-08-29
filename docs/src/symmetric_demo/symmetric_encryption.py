from cryptography.fernet import Fernet


key = Fernet.generate_key()
cipher = Fernet(key)

print("Secret Key:", key.decode())


message = "Hello, this is a secret message!"
encrypted_message = cipher.encrypt(message.encode())
print("Encrypted Message:", encrypted_message.decode())


decrypted_message = cipher.decrypt(encrypted_message).decode()
print("Decrypted Message:", decrypted_message)
