import unittest
from crypt import crypt

class TestCrypt(unittest.TestCase):
    def test_crypt(self):
        "Vérifie que la fonction crypt(message) existe et renvoie quelque chose"
        message = "abc"
        result = crypt(message)
        print(result)
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()