import nltk
from nltk import CFG
from nltk import grammar, parse
# from nltk.parse.generate import generate
from random import choice
from .tokenizer import Tokenizer

class Grammar():
    def __init__(self, rules):
        self.grammar = CFG.fromstring(rules)
        self.parser = nltk.ChartParser(self.grammar)
        self.tokenizer = Tokenizer(self.grammar)
    
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
        
    def parse_sentence(self, sentence):
        """
        This function is used to parse a sentence
        """
        try:
            tokens, unseen_tokens = self.tokenizer.tokenize(sentence)
            if len(unseen_tokens) > 0:
                return "()"
            
            tree = next(self.parser.parse(tokens))
            return tree.pformat(margin=float('inf'))
        except StopIteration:
            return "()"
        