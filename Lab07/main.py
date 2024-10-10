#Author: Phuong Tran, Leslie Lopez Arjon, Robert Oceguera
#Date: 10/07/2024
#Description: a program that allows the user to encrypt or decrypt messages using different types of encryption methods. 
#             Encrypted messages will read from the console and then written to a file called ‘message.txt’, and decrypted messages will be read from the ‘message.txt’ file then displayed to the console.
import check_input
import cipher
import caesar

def main():
    choice = check_input.get_int_range("Secret Decoder Ring: \n1.Encrypt \n2.Decrypt \n",1,2)
    if choice == 1:
        #Encrypt: read from console -> write to file
        file = open("message.txt", 'w')
        _type = check_input.get_int_range("Enter Encryption type: \n1. Atbash \n2. Caesar \n",1,2)
        message = input("Enter message: ").upper()

        if _type == 1: #atbash
            alphabet = cipher.Cipher()
            file.write(f"{alphabet.encrypt_message(message)}")

        if _type == 2: #caesar
            shift = check_input.get_int_range("Enter shift value (0-25): ", 0, 25)
            alphabet = caesar.Caesar(shift)
            file.write(f"{alphabet.encrypt_message(message)}")

        file.close()
    
    elif choice == 2:
        #Decrypt: read from file -> write to console
        file = open("message.txt")
        _type = check_input.get_int_range("Enter Decryption type: \n1. Atbash \n2. Caesar \n",1,2)
        message = file.readline()

        if _type == 1: #atbash
            alphabet = cipher.Cipher()
            print(alphabet.decrypt_message(message))
        if _type == 2: #caesar
            shift = check_input.get_int_range("Enter shift value (0-25): ", 0, 25)
            alphabet = caesar.Caesar(shift)
            print(alphabet.decrypt_message(message))

        file.close()
    
main()