import os
from app import Grammar

grammar_path = "./output/grammar.txt"
samples_path = "./output/samples.txt"

if __name__ == '__main__':
    grammar = Grammar(path=grammar_path)
    sentences = []
    for i in range(9999):
        new_sentence = ' '.join(grammar.generate_sentence())
        sentences.append(new_sentence)
    with open(samples_path, 'w') as f:
        f.write('\n'.join(sentences))
    print(sentences)