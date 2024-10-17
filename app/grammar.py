import nltk
from nltk import CFG
from nltk import grammar, parse
# from nltk.parse.generate import generate
from random import choice

class Grammar():
    def __init__(self, path):
        with open(path, 'r') as f:
            rules = f.read() 
        self.grammar = CFG.fromstring(rules)
        self.parser = nltk.ChartParser(self.grammar)
    
    def generate_sentence(self, symbols=None):
        if symbols is None:
            symbols = [self.grammar.start()]
        
        sentences = []
        if len(symbols) == 1:
            if isinstance(symbols[0], grammar.Nonterminal):
                rand_prod = choice(self.grammar.productions(lhs=symbols[0]))
                sentences += self.generate_sentence(rand_prod.rhs())
            else:
                sentences.append(symbols[0])
        else:
            for sym in symbols:
                sentences += self.generate_sentence([sym])
        return sentences    
        
    def parse_sentence():
        pass
        