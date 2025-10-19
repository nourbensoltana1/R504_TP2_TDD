import unittest
from decrypt import decrypt

class TestDecrypt(unittest.TestCase):
    def test_Decrypt(self):
        crypto = "acd"
        result = decrypt(crypto)
        print(result)
        self.assertEqual(result,' bc')

if __name__ == "__main__":
    unittest.main()