'''
Created on 09/18/2014

@author: vivek
'''

class MyString(object):
    """String manipulations"""

    def reverse(self, input_string):
        """
        Parameters:
            input_string: The string to reverse.
        Returns:
            Reversed string.
        """
        # list[start::end::step]
        return "".join(list(input_string)[::-1])

    def count_vowels(self, input_string):
        """
        Parameters:
            input_string: The string to count vowels in.
        Returns:
            Map {vowel: count}.
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        res = {char: 0 for char in vowels}
        for each in list(input_string):
            if each in vowels:
                res[each]+= 1
        return res

    def count_words(self, input_string):
        """
        Parameters:
            input_string: The string to count words in.
        Returns:
            The number of words.
        """
        return len(input_string.split())

    def is_palindrome(self, input_string):
        """
        Parameters:
            input_string: The input string.
        Returns:
            Whether the string is palindrome or not.
        """
        return self.reverse(input_string) == input_string

    def encrypt(self, input_string, shift=0):
        """
        Parameters:
            input_string: The string to encrypt.
            [a, b, c] = [0, 1, 2]
        Returns:
            The cipher text.
        """

        def get_encrypt_code(char):
            code = None
            if char.isupper():
                code = (ord(char) - ord('A') + shift) % 26 + ord('A')
            else:
                code = (ord(char) - ord('a') + shift) % 26 + ord('a')
            return code

        res = ''
        for char in input_string:
            if char.isalpha():
                code = get_encrypt_code(char)
            elif ord(char) == 32: # space character
                code = 32
            res += chr(code)
        return res


if __name__ == '__main__':
    myString = MyString()
    input_string = 'Foo Bar'
    print myString.reverse(input_string)
    print myString.count_vowels(input_string)
    print myString.count_words(input_string)
    print myString.is_palindrome('MADAM')
    print myString.encrypt('QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD', 3)
