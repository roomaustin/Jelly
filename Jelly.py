import cryptography
from cryptography.fernet import Fernet

# Key generation for encryption
def generate_key():
    return Fernet.generate_key()

# Encrypt a message
def encrypt_message(key, message):
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

# Decrypt a message
def decrypt_message(key, encrypted_message):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message

if __name__ == "__main__":
    # Agent generates a secret key
    secret_key = generate_key()
    
    while True:
        print("1. Send Encrypted Message")
        print("2. Decrypt Message")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            message = input("Enter the message to encrypt: ")
            encrypted_message = encrypt_message(secret_key, message)
            print(f"Encrypted Message: {encrypted_message}")
        
        elif choice == "2":
            encrypted_message = input("Enter the encrypted message: ")
            decrypted_message = decrypt_message(secret_key, encrypted_message)
            print(f"Decrypted Message: {decrypted_message}")
        
        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please choose a valid option.")
