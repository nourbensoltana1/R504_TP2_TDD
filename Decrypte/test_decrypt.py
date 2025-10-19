import unittest
from decrypt import decrypt
from crypt import crypt

class TestDecrypt(unittest.TestCase):
    def test_Decrypt(self):
        message=" ce"
        crypto = crypt(message,3)
        print (crypto)
        result = decrypt(crypto)
        print(result)
        self.assertEqual(result,message)

if __name__ == "__main__":
    unittest.main()