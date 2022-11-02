import unittest

from ST import SymbolTable


class MyTestCase(unittest.TestCase):
    def test_Addition(self):
        st = SymbolTable()
        st.addSymbolToST(2)
        self.assertEqual(st.getPositionOfSymbol(2), 10)
        self.assertNotEqual(st.addSymbolToST(2), 10)
        self.assertEqual(st.addSymbolToST(2), -1)

    def test_getSymbol_givenNonExistingSymbol(self):
        st = SymbolTable()
        self.assertEqual(st.getPositionOfSymbol(1), -1)


