from FiniteAutomata import FiniteAutomata
from Grammar import Grammar
from Parser import Parser
from ParserOutput import ParserOutput

from Scanner import Scanner
from Tree import Tree

if __name__ == '__main__':
    # scanner = Scanner()
    # st, pif, message = scanner.scan("input/Lab1a - p3.txt")
    # fa = FiniteAutomata('input/constant-integer.in')
    # fa.start()

    # parser = Parser("input/g1.txt")
    # grammar=Grammar("input/g1.txt")
    # grammar.start()

    seq = input("Input sequence for parser: ")
    parserOutput = ParserOutput("input/g1.txt")
    parserOutput.parse(seq)
    #tree=Tree("input/g1.txt")
