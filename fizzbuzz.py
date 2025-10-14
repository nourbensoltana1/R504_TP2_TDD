class FizzBuzz:
    def affiche(self,n=100):
        res=""
        for i in range(1, n+1):
            for i in range(1, 101):
                if i % 15 == 0:
                    res += "FrisBee"
                elif i % 5 == 0:
                    res += "Buzz"
                elif i % 3 == 0:
                    res += "Fizz"
                else:
                    res += str(i)
        return res
