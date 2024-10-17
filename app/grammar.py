import nltk
from nltk import CFG
from nltk import grammar, parse
# from nltk.parse.generate import generate
from random import choice

rules = """
% start S
S -> NP VP
S -> NP VP PerNoun

NP -> Pronoun | PreDet Nominal
VP -> Tense VP1 | VP2 | Tense VP3 | Passive VP1
VP1 -> Neg Verb Nominal | Verb Nominal | Verb Adverb | Verb PP
VP2 -> Adjective Adverb
VP3 -> Verb Adverb Conjunction Verb Nominal

Nominal -> Noun | Noun PosDet
Noun -> 'nhu cầu' | 'sản phẩm' | 'dịch vụ' | 'thông tin'
PosDet -> 'này' | 'kia' | 'đó' | 'ấy'
PreDet -> 'cái'
PerNoun -> 'anh' | 'chị' | 'bạn' | 'cậu' | 'chú' 
Verb -> 'có' | 'muốn' | 'thích' | 'cần' | 'biết' | 'mua' | 'thử'
Neg -> 'không'
Adverb -> 'lắm' | 'thêm'
Adjective -> 'bận' | 'hào hứng' | 'quan tâm'
Pronoun -> 'tôi' | 'mình' | 'tớ' | 'anh' | 'chị' | 'bạn' | 'cậu' | 'chú'

Conjunction -> 'và' | 'hoặc' | 'nhưng'
Tense -> 'đang' | 'vẫn' | 'sẽ' | 'đã'
Passive -> 'được' | 'bị'
PP -> 'về sản phẩm' | 'về dịch vụ'
Punc -> '.'
"""

class Grammar():
    def __init__(self):
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
        