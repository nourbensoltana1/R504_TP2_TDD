import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(FizzBuzz,unittest.TestCase):

    def test_affiche_exists(self):
        """Vérifie que la méthode affiche() existe et renvoie quelque chose"""
        result = self.affiche()  # appel de la méthode
        self.assertIn("1", result)
        self.assertIn("2", result)
        self.assertIn("100", result)
if __name__ == "__main__":
    unittest.main()
