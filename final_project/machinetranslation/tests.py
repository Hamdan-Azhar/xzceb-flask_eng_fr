import unittest
from translator import englishToFrench,frenchToEnglish

class TestTranslator(unittest.Testcase):
    
    def testEnglishToFrench(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')

    def testFrenchToEnglish(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')


if __name__ == '__main__':
    unittest.main()