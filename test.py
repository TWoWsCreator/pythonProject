class Fraction:
    def __init__(self, *args):
        if len(args) == 1:
            self._num, self._den = [int(num) for num in args[0].split('/')]
            # self.value = args[0]
        else:
            self._num, self._den = args[0], args[1]
            # self.value = (self._num, self._den)
        self._reduce_fraction()

    def _reduce_fraction(self):
        if (self._den < 0) and (self._num > 0):
            self._num, self._den = -self._num, -self._den
        k = max(self._num, self._den)
        while k != 1:
            if self._num % k == 0 and self._den % k == 0:
                self._num //= k
                self._den //= k
                break
            else:
                k -= 1

    def numerator(self, number=0):
        if number == 0:
            return self._num
        else:
            self._num = number
            self._reduce_fraction()

    def denominator(self, number=0):
        if number == 0:
            return self._den
        else:
            self._den = number
            self._reduce_fraction()

    def __str__(self):
        return f'{self._num}/{self._den}'

    def __repr__(self):
        return f"Fraction('{self._num}/{self._den}')"

    def __neg__(self):
        return Fraction(-self._num, self._den)

    def __add__(self, other):
        return Fraction(self._num * other._den + other._num * self._den, self._den * other._den)

    def __iadd__(self, other):
        self._num = self._num * other._den + other._num * self._den
        self._den = other._den * self._den
        self._reduce_fraction()
        return self

    def __sub__(self, other):
        return Fraction(self._num * other._den - other._num * self._den, self._den * other._den)

    def __isub__(self, other):
        self._num = self._num * other._den - other._num * self._den
        self._den = other._den * self._den
        self._reduce_fraction()
        return self


a = Fraction(1, 3)
b = Fraction(1, 2)
c = a + b
print(a, b, c, a is c, b is c)