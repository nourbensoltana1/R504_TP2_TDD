import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(FizzBuzz,unittest.TestCase):

    def test_affiche_exists(self):
        """Vérifie que la méthode affiche() existe et renvoie quelque chose"""
        result = self.affiche()  # appel de la méthode
        self.assertIn("Buzz", result)
        self.assertIn("5", result)
if __name__ == "__main__":
    unittest.main()
