def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                alphabet = 'abcdefghijklmnopqrstuvwxyz'
            else:
                alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            shifted_index = (alphabet.index(char) + shift * mode) % 26
            result += alphabet[shifted_index]
        else:
            result += char
    return result

def main():
    while True:
        choice = input("Would you like to encrypt or decrypt a message? (encrypt/decrypt): ").lower()
        if choice not in ['encrypt', 'decrypt']:
            print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")
            continue
        
        message = input("Enter the message: ")
        shift = int(input("Enter the shift value: "))
        
        if choice == 'encrypt':
            encrypted_message = caesar_cipher(message, shift, 1)
            print("Encrypted message:", encrypted_message)
        else:
            decrypted_message = caesar_cipher(message, shift, -1)
            print("Decrypted message:", decrypted_message)
        
        another = input("Do you want to encrypt/decrypt another message? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
