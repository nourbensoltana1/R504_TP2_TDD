class FizzBuzz:
    def affiche(self):
        res=""
        for i in range(1, 101):
            for i in range(1, 101):
                if i % 15 == 0:
                    res += "FrisBee"
                elif i % 5 == 0:
                    res += "Buzz"
                elif i % 15 == 0:
                    res += "Fizz"
                else:
                    res += str(i)
        return res
