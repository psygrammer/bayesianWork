import unittest


def add(a, b):
    sum = a
    for i in range(b):
        sum += 1
    return sum


class AddTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(2, add(1, 1))
        self.assertEqual(3, add(1, 2))


if __name__ == '__main__':
    unittest.main()
