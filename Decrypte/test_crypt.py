import unittest
from crypt import crypt

class TestCrypt(unittest.TestCase):
    def test_crypt(self):
        "Vérifie que la fonction crypt(message) existe et renvoie quelque chose"
        message = "ab7"
        result = crypt(message,5)
        print(result)
        self.assertEqual(result,'fgb5')

if __name__ == "__main__":
    unittest.main()