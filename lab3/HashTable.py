class HashTable:
    def __init__(self):
        self._size = 40
        self._ht = {}
        for i in range(self._size):
            self._ht[i] = []

    def getSize(self):
        return self._size

    def getSymbolOnPos(self, pos):
        return self._ht[pos]

    def hashFunction(self, symbol):  # sum of ascii characters % size of hash table
        sumAscii = 0
        for i in range(len(str(symbol))):
            sumAscii += ord(str(symbol)[i])
        return sumAscii % self._size

    def getPositionInSt(self, symbol):
        return self.hashFunction(symbol)

    def addSymbolToHT(self, symbol):
        positionInST = self.getPositionInSt(symbol)
        if symbol in self._ht[positionInST]:
            return -1
        self._ht[positionInST].append(symbol)
        return positionInST

    def getPositionOfSymbol(self, symbol):
        positionInSt = self.getPositionInSt(symbol)
        if len(self._ht[positionInSt]) == 0:
            return -1
        return positionInSt
