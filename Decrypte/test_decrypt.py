import unittest
from decrypt import decrypt

class TestDecrypt(unittest.TestCase):
    def test_Decrypt(self):
        crypto = "bcd"
        result = decrypt(crypto)
        print(result)
        self.assertEqual(result,'abc')

if __name__ == "__main__":
    unittest.main()