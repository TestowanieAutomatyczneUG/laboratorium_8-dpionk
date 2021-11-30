import unittest
from sample.FizzBuzz import *
from parameterized import parameterized, parameterized_class

class FizzBuzzParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = FizzBuzz()

    @parameterized.expand ([
    (5, "Buzz"),
    (3, "Fizz"),
    (15, "FizzBuzz"),
    (-5, "Buzz"),
    (-3, "Fizz"),
    (-30, "FizzBuzz"),
    (0, "FizzBuzz"),
    (7, "7"),
    (-7, "-7"),
    ])
    def test_parameterized_correct(self, number, expected):
        self.assertEqual(self.tmp.game(number), expected)

    @parameterized.expand([
    ('game', []),
    ('game', {}),
    ('game', 3.14)
])
    def test_parameterized_class_wrong(self, game, argument):
        self.assertRaises(ValueError, self.tmp.game, argument)



#Dodatkowe zadanie
@parameterized_class(('number', 'expected'), [
    (5, "Buzz"),
    (3, "Fizz"),
    (15, "FizzBuzz"),
    (-5, "Buzz"),
    (-3, "Fizz"),
    (-30, "FizzBuzz"),
    (0, "FizzBuzz"),
    (7, "7"),
    (-7, "-7"),
])

class FizzBuzzParameterizedPackage_2(unittest.TestCase):
    def setUp(self):
        self.tmp = FizzBuzz()

    def test_parameterized_class_correct(self):
        self.assertEqual(self.tmp.game(self.number), self.expected)


@parameterized_class(('function', 'argument'), [
    ('game', []),
    ('game',{}),
    ('game',3.14)
])
class FizzBuzzParameterizedPackage_3(unittest.TestCase):

    def setUp(self):
        self.tmp = FizzBuzz()

    def test_parameterized_class_wrong(self):
        self.assertRaises(ValueError, self.tmp.game, self.argument )





if __name__ == '__main__':
    unittest.main()
