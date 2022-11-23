class Grammar:
    def __init__(self, fileName):
        self._nonTerminals = []
        self._terminals = []
        self._productions = {}
        self._S = ""
        self.readFromFile(fileName)

    def readFromFile(self, fileName):
        with open(fileName, 'r') as file:
            nonterminals = file.readline()
            self._nonTerminals = nonterminals[6:-2]

            terminals = file.readline()
            self._terminals = terminals[6:-2]

            self._S = file.readline()[4:-1]

            file.readline()
            while True:
                line = file.readline()
                if len(line) == 1:
                    break
                line = line.strip().split('->')
                nonTerminal = line[0].strip()
                productions = line[1].strip().split("|")
                newProductions = []

                for p in productions:
                    p = p.strip().split(" ")
                    newProductions.append(p)

                self._productions[nonTerminal] = newProductions

    def checkCGF(self):
        cfg = True
        for p in self._productions:
            if len(self._productions[p]) > 1:
                cfg = False
        return cfg


    def menu(self):
        print('1. Get nonterminals')
        print('2. Get terminals')
        print('3. Get productions')
        print('4. Get S')
        print('5. Get productions for a given nonTerminal')
        print('6. CFG check')
        print('0. Exit')

    def start(self):
        while True:
            self.menu()
            try:
                inp = int(input('Enter your choice: '))
            except ValueError:
                print("Not a valid input type.")
                break
            if inp == 1:
                print("The nonterminals are: ", self._nonTerminals)
            elif inp == 2:
                print("The terminals are: ", self._terminals)
            elif inp == 3:
                print("The productions are: ", self._productions)
            elif inp == 4:
                print("S is : ", self._S)
            elif inp == 5:
                print("The productions for a given nonterminal are: ")
                nonterminal = input("Enter the wanted nonTerminal:")
                print(self._productions[nonterminal])
            elif inp == 6:
                if self.checkCGF():
                    print("\nIs CFG\n")
                else:
                    print("\nIs not CFG\n")
            else:
                break

