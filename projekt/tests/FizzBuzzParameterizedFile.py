import unittest
from sample.FizzBuzz import *

class FizzBuzzTest(unittest.TestCase):

    def test_from_file(self):
        file = open("data/FizzBuzz_data_test")
        temp = FizzBuzz()
        for line in file:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(" ")
                if data[0].strip("\n") == "tablica":
                    self.assertRaises(ValueError, temp.game, [])
                elif data[0].strip("\n") == "obiekt":
                    self.assertRaises(ValueError, temp.game, {})
                elif data[0].strip("\n") == "float":
                    self.assertRaises(ValueError, temp.game, 3.14)
                else:
                    self.assertEqual(temp.game(int(data[0])), data[1].strip("\n") )

        file.close()

if __name__ == '__main__':
    unittest.main()