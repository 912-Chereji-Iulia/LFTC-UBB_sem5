
from prettytable import PrettyTable
class PIF:
    def __init__(self):
        self._pif = []

    def addToPIF(self, token, st_pos):
        pair = (token, st_pos)
        self._pif.append(pair)

    def __str__(self):
        result = 'PIF \n------------------- \n' + '|TOKEN   |  ST_POS |\n' + '------------------- \n'
        for pair in self._pif:
            result = result + "|" + str(pair[0]) + "     |     " + str(pair[1]) + "  |" + '\n'
        result += '-------------------'
        return result
