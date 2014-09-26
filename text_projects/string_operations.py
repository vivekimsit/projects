'''
Created on 09/18/2014

@author: vivek
'''

class MyString(object):
    """String manipulations"""

    def reverse(self, aString):
        """
        Parameters:
            aString: The string to reverse.
        Returns:
            Reversed string.
        """
        # list[start::end::step]
        return "".join(list(aString)[::-1])

    def count_vowels(self, aString):
        """
        Parameters:
            aString: The string to count vowels in.
        Returns:
            Map {vowel: count}.
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        res = {char: 0 for char in vowels}
        for each in list(aString):
            if each in vowels:
                res[each]+= 1
        return res

    def count_words(self, aString):
        """
        Parameters:
            aString: The string to count words in.
        Returns:
            The number of words.
        """
        return len(aString.split())

    def is_palindrome(self, aString):
        """
        Parameters:
            aString: The input string.
        Returns:
            Whether the string is palindrome or not.
        """
        return self.reverse(aString) == aString

    def encrypt(self, aString, shift=0):
        """
        Parameters:
            aString: The string to encrypt.
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
        for char in aString:
            if char.isalpha():
                code = get_encrypt_code(char)
            elif ord(char) == 32: # space character
                code = 32
            res += chr(code)
        return res


if __name__ == '__main__':
    myString = MyString()
    aString = 'Foo Bar'
    print myString.reverse(aString)
    print myString.count_vowels(aString)
    print myString.count_words(aString)
    print myString.is_palindrome('MADAM')
    print myString.encrypt('QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD', 3)
