import nltk
from nltk import CFG
from nltk import grammar
# from nltk.parse.generate import generate
from random import choice
from models import Tokenizer, TopDownParser

class Grammar():
    def __init__(self, rules):
        self.grammar = CFG.fromstring(rules)
        self.parser = TopDownParser(self.grammar)
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
            tokens, unk_tokens = self.tokenizer.tokenize(sentence)
            if len(unk_tokens) > 0:
                return "()"
            tree = self.parser.parse(tokens)
            return self.parser.penn_tree_bank_format(tree)

        except StopIteration:
            return "()"
        
    def built_in_parser(self, sentence):
        """
        This function is used to parse a sentence using NLTK built-in parser
        """
        try:
            tokens, unk_tokens = self.tokenizer.tokenize(sentence)
            if len(unk_tokens) > 0:
                return "()"
            parser = nltk.ChartParser(self.grammar)
            tree = next(parser.parse(tokens))
            return tree.pformat(margin=1000000)
        except StopIteration:
            return "()"
        