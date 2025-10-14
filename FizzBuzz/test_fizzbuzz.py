import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(FizzBuzz,unittest.TestCase):

    def test_affiche_exists(self):
        """Vérifie que la méthode affiche() existe et renvoie quelque chose"""
        result = self.affiche(15,20)  # appel de la méthode
        print(result)
if __name__ == "__main__":
    unittest.main()
