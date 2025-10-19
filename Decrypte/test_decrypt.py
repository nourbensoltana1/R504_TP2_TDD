import unittest
from decrypt import decrypt

class TestDecrypt(unittest.TestCase):
    def test_Decrypt(self):
        crypto = "cfh"
        result = decrypt(crypto,3)
        print(result)
        self.assertEqual(result,' ce')

if __name__ == "__main__":
    unittest.main()