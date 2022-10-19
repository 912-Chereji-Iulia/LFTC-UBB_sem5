from ST import SymbolTable
if __name__ == '__main__':
    st = SymbolTable()
    nr = 4
    st.addSymbolToST("iulia")
    st.addSymbolToST("$(")
    st.addSymbolToST("ola")
    st.addSymbolToST(2)
    st.addSymbolToST(nr)
    print(st)
    print("Position of 1:", st.getPositionOfSymbol(1))
    print("Position of nr:", st.getPositionOfSymbol(nr))
    print("Position of 'ola':", st.getPositionOfSymbol('iulia'))
