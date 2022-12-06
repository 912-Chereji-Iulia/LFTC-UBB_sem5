import unittest

from Parser import Parser


class MyTestCase(unittest.TestCase):
    def testCanonicalCollection(self):
        parser = Parser("input/g1.txt")
        print(parser.computeCanonicalCollection())
        self.assertEqual(parser.computeCanonicalCollection().pop(1), [("S'", ['S.'])])
        self.assertNotEqual(parser.computeCanonicalCollection().pop(0), [("S'", ['.aA'])])
        self.assertEqual(parser.computeCanonicalCollection().pop(0), [("S'", ['.S']), ('S', ['.aA'])])

if __name__ == '__main__':
    unittest.main()
