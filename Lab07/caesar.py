#Author: Phuong Tran, Leslie Lopez Arjon, Robert Oceguera
#Date: 10/07/2024
#Description: Subclass Caesar inheritance from super class Cipher
import cipher
class Caesar(cipher.Cipher):
    """ Represent a substitution cipher where the encrypted message is found by 
        looking up each letter and finding the corresponding letter in a shifted alphabet
        Attributes:
            _shift (int): the value to shift the letter in the message
        Methods:
            __init__(self, shift): passes in caesar cipher shift value. Call super to initialize the alphabet, then set the shift value
            _encrypt_letter(self, letter): overridden method. passes in one character or letter. Look up the letter in the alphabet to find its location. Use that location to calculate the position of the encrypted letter in the manner described above, then return the encrypted letter.
            _decrypt_letter(self, letter): overridden method. passes in one character, letter. Look up the letter in the alphabet to find its location. Use that location to calculate the position of the decrypted letter in the manner described above, then return the decrypted letter.
                                        
    """
    def __init__(self, shift: int):
        """
        Initialize the Caesar cipher with a shift value.

        Args:
            shift (int): The number of positions to shift the alphabet.
        """
        super(Caesar, self).__init__()
        self._shift = shift

    def _encrypt_letter(self, letter):
        """
        Encrypt a single letter using the Caesar cipher.

        Args:
            letter (str): The letter to encrypt.

        Returns:
            str: The encrypted letter.
        """
        if letter not in self._alphabet:
            return letter
        index = self._alphabet.find(letter)
        new_index = (index + self._shift) % 26
        return self._alphabet[new_index]

    def _decrypt_letter(self, letter):
        """
        Decrypt a single letter using the Caesar cipher.

        Args:
            letter (str): The letter to decrypt.

        Returns:
            str: The decrypted letter.
        """
        if letter not in self._alphabet:
            return letter
        index = self._alphabet.find(letter)
        new_index = (index - self._shift) % 26
        return self._alphabet[new_index]

