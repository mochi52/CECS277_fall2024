#Author: Phuong Tran, Leslie Lopez Arjon, Robert Oceguera
#Date: 10/07/2024
#Description: Super Class Cipher
class Cipher:
    """ Represents a substitution cipher where the encrypted message is obtained by looking up each letter and finding the corresponding letter in a reversed alphabet.
        Attributes:
            _alphabet (str): string of alphabet letters
        Methods:
            __init__ (self): initializes the alphabet attribute 
            encrypt_message(self, message): Convert the message to upper case letters, then loop through the message string one character at a time, if it is
                                            a letter A-Z, then call the encrypt_letter method, otherwise ignore the character
            decrypt_message(self, message): Convert the message to upper case letters, then loop through the message string one character at a time, if it is
                                            a letter A-Z, then call the decrypt_letter method, otherwise ignore the character
            _encrypt_letter(self, letter):  passes in one character, letter. Look up the letter
                                            in the alphabet to find its location. Use that location to calculate the position of the
                                            encrypted letter in the manner described above, then return the encrypted letter.               
            _decrypt_letter(self, letter):  passes in one character, letter. Look up the letter
                                            in the alphabet to find its location. Use that location to calculate the position of the
                                            decrypted letter in the manner described above, then return the decrypted letter.    
    """
    def __init__ (self):
        """Initialize the cipher with the alphabet."""

        self._alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def encrypt_message(self, message: str) -> str:
        """
        Encrypt the given message.

        Args:
            message (str): The message to encrypt.

        Returns:
            str: The encrypted message.
        """
        _list = list(message)
        for i in range(len(_list)):
            if _list[i] not in self._alphabet:
                continue
            _list[i] = self._encrypt_letter(_list[i])

        encrypt_message = ""
        for i in _list:
            encrypt_message += i.upper()
        
        return encrypt_message

    def decrypt_message(self, message: str) -> str :
        """
        Decrypt the given message.

        Args:
            message (str): The message to decrypt.

        Returns:
            str: The decrypted message.
        """
        _list = list(message)
        for i in range(len(_list)):
            if _list[i] not in self._alphabet:
                continue
            _list[i] = self._decrypt_letter(_list[i])

        decrypt_message = ""
        for i in _list:
            decrypt_message += i.upper()
        
        return decrypt_message

    def _encrypt_letter (self, letter) :
        """
        Encrypt a single letter.

        Args:
            letter (str): The letter to encrypt.

        Returns:
            str: The encrypted letter.
        """
        index = self._alphabet.find(letter)
        new_index = 25 - index
        return self._alphabet[new_index]
        

    def _decrypt_letter (self, letter) :
        """
        Decrypt a single letter.

        Args:
            letter (str): The letter to decrypt.

        Returns:
            str: The decrypted letter.
        """
        index = self._alphabet.find(letter)
        new_index = 25 - index
        return self._alphabet[new_index]
