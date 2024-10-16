import nltk
from nltk import CFG
from nltk import grammar, parse
from nltk.parse.generate import generate

rules = """
% start S
S -> NP VP Punc

NP -> Pronoun | Noun
VP -> Verb NP

Noun -> 'nhu cầu'
Verb -> 'đang' | 'có'
Adverb -> 'lắm'
Adjective -> 'bận'
Pronoun -> 'tôi' | 'mình' | 'tớ' | 'anh' | 'chị' | 'bạn' | 'cậu' | 'chú'
Conjunction -> 'và' | 'hoặc' | 'nhưng'
Punc -> '.'
"""

class Grammar():
    def __init__(self):
        self.grammar = CFG.fromstring(rules)
        self.parser = nltk.ChartParser(self.grammar)
    
    def generate_sentence(self):
        for sentence in generate(self.grammar):
            print(' '.join(sentence))
            
        
    def parse_sentence():
        pass
        