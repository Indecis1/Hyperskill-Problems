import fractions

class Fraction:
    """
    A denormalized representation of a fraction
    """
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.repr = fractions.Fraction(numerator, denominator)

    def __repr__(self):
        return 'Fraction({}, {}) = {}'.format(self.numerator, self.denominator, self.repr)

    def __str__(self):
        return 'Fraction({}, {})'.format(self.numerator, self.denominator)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    __rmul__ = __mul__

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.repr < other.repr
        else:
            return self.repr < other

    def __le__(self, other):
        if isinstance(other, Fraction):
            return self.repr <= other.repr
        else:
            return self.repr <= other

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.repr == other.repr
        else:
            return self.repr == other

    def __ne__(self, other):
        if isinstance(other, Fraction):
            return self.repr != other.repr
        else:
            return self.repr != other

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.repr > other.repr
        else:
            return self.repr > other

    def __ge__(self, other):
        if isinstance(other, Fraction):
            return self.repr >= other.repr
        else:
            return self.repr >= other
