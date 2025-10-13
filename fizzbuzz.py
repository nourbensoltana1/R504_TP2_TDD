class FizzBuzz:
    def affiche(self):
        res=""
        for i in range(1, 101):
            for i in range(1, 101):
                if i % 3 == 0:
                    res += "Fizz"
                elif i % 5 == 0:
                    res += "Buzz"
                else:
                    res += str(i)
        return res
