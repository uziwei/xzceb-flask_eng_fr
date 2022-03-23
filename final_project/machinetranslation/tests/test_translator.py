import unittest

from translator import english_to_french, french_to_english

class frenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # Test for the translation of the word 'Bonjour' into English is equal to 'Hello'
        self.assertNotEqual(french_to_english('Oui'), 'Oui') # Test for the translation of the world 'Oui' into English is not equal to 'Oui'.

class englishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # Test for the translation of the word 'Hello' into French is equal to 'Bonjour'
        self.assertNotEqual(english_to_french('Yes'), 'Yes')  # Test for the translation of the world 'Yes' into French is not equal to 'Yes'.

unittest.main()
