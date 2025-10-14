import unittest
from main omport crypt

class TestCrypt(unittest.TestCase):
    def test_crypt-exists(self):
        """Vérifie que la fonction crypt(message) existe et renvoie quelque chose"""
        message = "abc"
        result = crypt(message)
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()