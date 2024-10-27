import nltk

class TopDownParser:
    def __init__(self, grammar):
        self.grammar = grammar  # The CFG grammar from NLTK
        self.start_symbol = grammar.start()  # Typically 'S'
        self.tokens = []
        self.index = 0  # Track current token index
        self.backtrack = []  # Stack to store backtracking points

    def parse(self, tokens):
        """
        Parse the tokens using recursive descent with backtracking.
        :param tokens: The list of tokens to parse (input sentence).
        :return: Parse tree if successful, None otherwise.
        """
        self.tokens = tokens
        self.index = 0  # Reset token index for new parsing attempt
        self.backtrack = []

        parse_tree = self._parse_symbol(self.start_symbol)
        
        if parse_tree and self.index == len(tokens):
            return parse_tree
        
        if self.backtrack and parse_tree:
            production, original_index = self.backtrack.pop()
            self.index = original_index
            self._parse_production(production.rhs(), parse_tree)
            return parse_tree
        
        return None  # Return None if parsing failed

    def _parse_symbol(self, symbol):
        """
        Recursively attempt to parse based on the current symbol.
        :param symbol: The current grammar symbol (either non-terminal or terminal).
        :return: Nested list representing parse tree if successful, None otherwise.
        """
        if isinstance(symbol, nltk.Nonterminal):  # If non-terminal, expand it
            productions = self.grammar.productions(lhs=symbol)
            for i in range(len(productions)):
                original_index = self.index  # Save current index for backtracking
                subtree = [symbol]  # Create a subtree for this symbol
                
                if i < len(productions) - 1 and isinstance(productions[i].rhs()[0], nltk.Nonterminal) and symbol != nltk.Nonterminal("S"):
                    self.backtrack.append((productions[i + 1], original_index))
                    
                if self._parse_production(productions[i].rhs(), subtree):  # Try expanding with this production
                    return subtree  # Return the subtree if successful
                else:
                    self.index = original_index  # Backtrack on failure
                    
            return None  # No production matched
        else:  # If terminal, try to match it with the current token
            if self.index < len(self.tokens) and symbol == self.tokens[self.index]:
                self.index += 1  # Consume the token
                return symbol
            else:
                return None  # Terminal did not match

    def _parse_production(self, rhs, subtree):
        """
        Recursively parse each symbol in the right-hand side of a production.
        :param rhs: The right-hand side symbols of a production.
        :param subtree: The current subtree being built for the production.
        :return: True if successfully matches all symbols in rhs, False otherwise.
        """
        for symbol in rhs:
            result = self._parse_symbol(symbol)  # Recursively parse each symbol
            if result is None:
                return False
            subtree.append(result)
        return True

    def penn_tree_bank_format(self, tree):
        """
        Pretty print the tree in a bracketed format similar to the Penn Treebank format.
        """
        if tree is None:
            return "()"
        
        if isinstance(tree, str):  # Leaf node (terminal)
            return tree
        else:
            symbol = tree[0]
            children = " ".join(self.penn_tree_bank_format(child) for child in tree[1:])
            return f"({symbol} {children})"