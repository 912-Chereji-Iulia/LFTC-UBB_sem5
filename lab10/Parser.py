from prettytable import PrettyTable

from Grammar import Grammar


class Parser:
    def __init__(self, filename):
        self._grammar = Grammar(filename)

    def closure(self, items):
        if not items:
            return None
        closure = items
        ok = True
        while ok:
            ok = False
            for item in closure:
                dotPos = item[1][0].index('.')
                afterDot = item[1][0][dotPos + 1:].strip()
                # if len(afterDot) > 0:
                #     firstAfterDot=""
                #     found=False
                #     i=0
                #     while found==False and i<len(afterDot):
                #         firstAfterDot+=afterDot[i]
                #         i+=1
                #         if len(firstAfterDot)>1:
                #
                #             if firstAfterDot in self._grammar.getNonTerminals().split(" ") or firstAfterDot in self._grammar.getTerminals().split(" "):
                #                 found=True
                if len(afterDot) > 0:

                    if (afterDot in self._grammar.getTerminals() or afterDot in self._grammar.getNonTerminals()):
                        firstAfterDot = afterDot
                    else:
                        firstAfterDot = afterDot[0]
                    if not self._grammar.isTerminal(firstAfterDot):
                        for prod in self._grammar.getProductionsForNonTerminal(firstAfterDot):
                            newProd = ""
                            for p in prod.split(" "):
                                if (p != " "):
                                    newProd += p
                            production = (firstAfterDot, ['.' + newProd])
                            if production not in closure:
                                closure.append(production)
                                ok = True

        return closure

    def goTo(self, state, symbol):
        # move the dot after symbol if symbol== first symbol after dot
        # then, return closure for this new item
        items = []
        for production in state:
            element = production[1][0]
            dotPos = element.index('.')
            beforeDot = element[:dotPos]
            afterDot = element[dotPos + 1:].strip().split(" ")

            if len(afterDot) != 0:
                if len(afterDot[0]) > 0:
                    firstSymbolAfterDot = afterDot[0][0]
                else:
                    firstSymbolAfterDot = ""

                rest = afterDot[0][1:]

                if firstSymbolAfterDot == symbol:
                    if len(rest) != 0:
                        newProd = (production[0], [beforeDot + firstSymbolAfterDot + '.' + rest[0]])
                    else:
                        newProd = (production[0], [beforeDot + firstSymbolAfterDot + '.'])
                    items += [newProd]

        return self.closure(items)

    def computeCanonicalCollection(self):
        initialProd = [('S\'', ['.' + self._grammar.getStartingSymbol()])]
        canonicalCollection = [self.closure(initialProd)]
        union = self._grammar.getNonTerminals() + " " + self._grammar.getTerminals()

        ccIsModified = True
        while ccIsModified:
            ccIsModified = False
            for state in canonicalCollection:
                for x in union.split(" "):
                    nextState = self.goTo(state, x)
                    if nextState is not None and nextState not in canonicalCollection:
                        canonicalCollection += [nextState]
                        ccIsModified = True
        return canonicalCollection

    def toStringCanonicalCollection(self):
        print("Canonical collection: ")
        pos = 0
        for c in self.computeCanonicalCollection():
            print("S" + str(pos) + "=", c, "\n")
            pos += 1

    def getTable(self):
        states = self.computeCanonicalCollection()
        table = []
        for i in range(len(states)):
            table.append({})

        stateNr = 0
        for state in states:
            shift = 0
            reduce = 0
            accept = 0
            nrOfProductionsForState = len(state)
            elemInTable = table[stateNr]

            for prod in state:
                element = prod[1][0]
                dotPos = element.index('.')
                beforeDot = element[:dotPos]
                afterDot = element[dotPos + 1:].strip()

                if len(afterDot) == 0:
                    # dot is at the end for prod. of S’
                    if prod[0] == 'S\'' and beforeDot == self._grammar.getStartingSymbol():
                        accept += 1

                    # dot is at the end, but not for S’
                    elif prod[0] != 'S\'':
                        reduce += 1
                        elem = [prod[0], beforeDot]
                        productionPos = self._grammar._prodList.index(elem)
                else:
                    # dot is not at the end
                    shift += 1

            # one column for action/state (for a state, action is unique because prediction is ignored)
            if shift == nrOfProductionsForState:
                elemInTable['ACTION'] = 'shift'

            elif reduce == nrOfProductionsForState:
                elemInTable['ACTION'] = 'reduce' + str(productionPos + 1)

            elif accept == nrOfProductionsForState:
                elemInTable['ACTION'] = 'accept'
            else:
                raise (Exception('error for state ' + str(state)))

            # goto: one column for each symbol in N+T
            union = self._grammar.getNonTerminals() + self._grammar.getTerminals()
            for symbol in union:
                nextState = self.goTo(state, symbol)
                if nextState in states:
                    indexOfNextState = states.index(nextState)
                    elemInTable[symbol] = indexOfNextState
            stateNr += 1

        return table

    def toStringTable(self):
        table = self.getTable()
        result = PrettyTable(['STATE', 'ACTION', 'GOTO'])
        stateNr = 0
        for pair in table:
            for k in pair.keys():
                for v in pair.values():
                    if (pair.get(k) == v):
                        if k == 'ACTION':
                            result.add_row([stateNr, str(v), " "])
                        else:
                            result.add_row([stateNr, "", str(k) + ": s" + str(v)])
            stateNr += 1

        return str(result)
