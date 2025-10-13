import unittest
from fizzbuzz import affiche

class TestFizzBuzz(unittest.TestCase):
    def test_affiche_exists(self):
        """Vérifie que la fonction affiche() existe et renvoie quelque chose"""
        result = affiche()
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()
