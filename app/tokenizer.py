class Tokenizer():
    def __init__(self, cfg):
        self.token_set = self.extract_tokens(cfg)
           
    def extract_tokens(self, cfg):
        token_set = set()
        for prod in cfg.productions():
            for symbol in prod.rhs():
                if isinstance(symbol, str):
                    token_set.add(symbol)
        return sorted(token_set, key=lambda x: -len(x)) # prioritize longer tokens

    def tokenize(self, sentence):
        tokens = []
        unseen_tokens = []
        curr_str = sentence
        while curr_str:
            is_matched = False
            for token in self.token_set:
                if curr_str.startswith(token):
                    tokens.append(token)
                    curr_str = curr_str[len(token):].strip()
                    is_matched = True
                    break
            if not is_matched:
                unseen_token = curr_str.split(' ')[0]
                tokens.append(unseen_token)
                unseen_tokens.append(unseen_token) # add to unseen_tokens list
                curr_str = curr_str[len(unseen_token):].strip()
        return tokens, unseen_tokens
            