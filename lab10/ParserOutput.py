from Parser import Parser
from Table import Table


class ParserOutput:
    def __init__(self, filename):
        self.parser = Parser(filename)
        self.table = Table(filename)

    def displayParsingByDerivations(self, output):
        firstProduction = self.parser._grammar._prodList[int(output[0])]
        result = str(firstProduction[0]) + "=>(" + output[0] + ") " + str(firstProduction[1])
        initial = firstProduction[1]
        for state in output:
            if int(state) != 0:
                result += "=>(" + state + ") "
                currentProduction = self.parser._grammar._prodList[int(state)]
                left = currentProduction[0]
                right = currentProduction[1]
                initial = initial.replace(left, right, 1)
                result += initial
        print(result)
        return result

    def initialiseStacks(self, input):
        self.workStack = ['0']
        self.inputStack = []
        for symbol in input:
            self.inputStack.append(symbol)
        self.output = []

    def parse(self, input):
        table = self.table.getTable()
        print(self.table.toStringTable(table))

        self.initialiseStacks(input)

        while len(self.workStack) != 0:
            state = int(self.workStack[-1])
            if len(self.inputStack) > 0:
                symbol = self.inputStack.pop(0)
            else:
                symbol = None
            try:
                self.checkActionForSymbol(symbol, table, state)
            except Exception as e:
                print(e)
                return


        result = self.displayParsingByDerivations(self.output)
        self.writeToFile("output/parserOutput.out", result)

    def shift(self, symbol, table, state):
        self.workStack.append(symbol)
        self.workStack.append(str(table[state][symbol]))

    def accept(self):
        if (len(self.inputStack)) != 0:
            raise Exception("something went wrong")
        self.workStack = []

    def reduce(self, table, state):
        try:
            rIndex = int(table[state]["ACTION"][-1])
        except:
            print("Can't be parsed")
        production = self.parser._grammar._prodList[rIndex]
        self.workStack.pop()
        removeFromWorkStack = []

        for symbol in production[1]:
            removeFromWorkStack.append(symbol)

        while len(removeFromWorkStack) > 0 and len(self.workStack) > 0:

            if self.workStack[-1].isnumeric():
                self.workStack.pop()

            if self.workStack[-1] == removeFromWorkStack[-1]:
                removeFromWorkStack.pop()

            self.workStack.pop()

        if len(removeFromWorkStack) != 0:
            raise (Exception('error at parsing reduce'))

        self.inputStack.insert(0, production[0])
        self.output.insert(0, str(rIndex))

    def checkActionForSymbol(self, symbol, table, state):
        global rIndex
        if symbol is not None:
            if symbol not in table[state]:
                raise Exception("Symbol " + symbol + " not in table for state " + str(state))
            elif table[state][symbol] is not None and table[state]["ACTION"] == "shift":
                self.shift(symbol,table,state)
        if symbol is None:
            if table[state]["ACTION"] == "accept":
               self.accept()
            else:
                self.reduce(table, state)

    def writeToFile(self, fileName, result):
        with open(fileName, 'w') as file:
            file.write(result)
