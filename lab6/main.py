from FiniteAutomata import FiniteAutomata
from Scanner import Scanner

if __name__ == '__main__':
    scanner = Scanner()
    st, pif, message = scanner.scan("input/Lab1a - p3.txt")
    fa = FiniteAutomata('input/identifier.in')
    fa.start()




