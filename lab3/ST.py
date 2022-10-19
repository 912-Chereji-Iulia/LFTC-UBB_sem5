from HashTable import HashTable


class SymbolTable:
    def __init__(self):
        self._size = 40
        self._st = []
        for i in range(self._size):
            self._st.append([])
        self._ht = HashTable()

    def getPositionInSt(self, symbol):
        return self._ht.hashFunction(symbol)

    def addSymbolToST(self, symbol):
        positionInST = self.getPositionInSt(symbol)
        if symbol in self._st[positionInST]:
            return -1
        self._st[positionInST].append(symbol)
        return positionInST, len(self._st[positionInST]) - 1

    def getPositionOfSymbol(self, symbol):
        positionInSt = self.getPositionInSt(symbol)
        if len(self._st[positionInSt]) == 0:
            return -1
        allSymbols = self._st[positionInSt]
        for posInList in range(len(allSymbols)):
            if allSymbols[posInList] == symbol:
                return positionInSt, posInList

    def __str__(self):
        result = 'Symbol Table \n------------------- \n' + '|ST_POS   |  SYMBOL |\n' + '------------------- \n'
        for pos in range(self._size):
            result = result + "|" + str(pos) + "     |     " + str(self._st[pos]) + "  |" + '\n'
        result += '-------------------'
        return result
