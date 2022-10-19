class HashTable:
    def __init__(self):
        self._size = 40

    def hashFunction(self, symbol):  # sum of ascii characters
        sumAscii = 0
        for i in range(len(str(symbol))):
            sumAscii += ord(str(symbol)[i])
        return sumAscii % self._size

