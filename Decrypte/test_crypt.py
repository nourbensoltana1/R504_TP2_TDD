import unittest
from crypt import crypt

class TestCrypt(unittest.TestCase):
    def test_crypt(self):
        "Vérifie que la fonction crypt(message) existe et renvoie quelque chose"
        message = "ab9"
        result = crypt(message,100)
        print(result)
        self.assertEqual(result,'cda2')

if __name__ == "__main__":
    unittest.main()