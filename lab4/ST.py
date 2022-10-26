from HashTable import HashTable


class SymbolTable:
    def __init__(self):
        self._ht = HashTable()

    def addSymbolToST(self, symbol):
        return self._ht.addSymbolToHT(symbol)

    def getPositionOfSymbol(self, symbol):
        return self._ht.getPositionOfSymbol(symbol)

    def getSize(self):
        return self._ht.getSize()

    def getSymbolOnPos(self, pos):
        return self._ht.getSymbolOnPos(pos)

    def __str__(self):
        result = 'Symbol Table \n------------------- \n' + '|ST_POS   |  SYMBOL |\n' + '------------------- \n'
        for pos in range(self.getSize()):
            result = result + "|" + str(pos) + "     |     " + str(self.getSymbolOnPos(pos)) + "  |" + '\n'
        result += '-------------------'
        return result
