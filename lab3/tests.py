import unittest

from ST import SymbolTable


class MyTestCase(unittest.TestCase):
    def test_Addition(self):
        st = SymbolTable()
        st.addSymbolToST(2)
        self.assertEqual(st.getPositionOfSymbol(2), 10)
