from app import Grammar

if __name__ == '__main__':
    grammar = Grammar()
    for i in range(1000):
        print(' '.join(grammar.generate_sentence()))