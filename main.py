import os
from app import Grammar

# Define relative paths to input and output files
grammar_path = "./output/grammar.txt"
samples_path = "./output/samples.txt"
input_sentences_path = "./input/sentences.txt"
parse_results_path = "./output/parse-results.txt"

# 2.2 Generate sentences
def generate_sentence(grammar, output_path):    
    with open(output_path, 'w') as output_file:
        sentences = []
        for _ in range(10000):
            new_sentence = ' '.join(grammar.generate_sentence())
            if new_sentence not in sentences: # avoid duplicate sentences
                sentences.append(new_sentence)
        output_file.write('\n'.join(sentences))

# 2.3 Parse sentences
def parse_sentence(grammar, input_path, output_path):
    with open(input_path, 'r') as input_file:
        input_sentences = input_file.read()
        list_sentences = input_sentences.split('\n')
        parse_results = []
        for sentence in list_sentences:
            result_sentence = grammar.parse_sentence(sentence)
            parse_results.append(result_sentence)
        with open(output_path, 'w') as output_file:
            output_file.write('\n'.join(parse_results))
    
if __name__ == '__main__':
    with open(grammar_path, 'r') as rules_file:
        rules = rules_file.read() 
        grammar = Grammar(rules=rules)
        # generate_sentence(grammar, samples_path)
        parse_sentence(grammar, input_sentences_path, parse_results_path)
    