import nltk
import string
import argparse
from nltk import load_parser
from file_manager import write_file
from data import retrive_data
from grammar_relation import create_grammar_relation
from semantic_procedure import create_semantic_procedure

def main(args):
    # Main entry point of program
    sentences = [
    "em có thể nhắc lại tất cả các tour được không",
    "đi từ Hồ Chí Minh tới Nha Trang hết bao lâu",
    "đi từ Hồ Chí Minh tới Đà Nẵng hết bao lâu",
    "có bao nhiêu tour đi Phú Quốc vậy bạn",
    "tour Nha Trang đi bằng phương tiện gì vậy",
    "đi Nha Trang có những ngày nào nhỉ"
    ]
    
    # Load grammar file
    print("Loading grammar file...")
    grammar_rule = load_parser(args.grammar_rule_file_name, trace=0)
    path = write_file(0, str(grammar_rule.grammar()))
    print(f"Grammar file loaded successfully. Grammar rules are saved at {path}")
    
    # Parse sentences and print semantic representation
    print("Parsing sentences and getting semantic presentations...")
    q2_content = ""
    sem_list = []
    tree_list = [] # Save for using later
    for idx, sentence in enumerate(sentences, 1):
        q2_content += f"Parsing sentence {idx}: {sentence}\n"
        tree = grammar_rule.parse_one(sentence.replace('?', '').split())
        if tree:
            tree_list.append(tree)
            parse_result = f"Parsed result of sentence {idx}: {str(tree.pformat(margin=float('inf')))}\n"
            semantic = f"Semantic of sentence {idx}: {str(tree.label()['SEM'])}"
            sem_list.append(str(tree.label()['SEM']))
            q2_content += parse_result + semantic + "\n"
        else:
            q2_content += f"Failed to parse sentence {idx}: {sentence}\n"
        q2_content += '\n'
    path = write_file(1, q2_content)
    print(f"Sentences parsed successfully. Results are saved at {path}")
    
    # Create grammar relation
    print("Creating grammar relation...")
    results = []
    for idx, sem in enumerate(sem_list):
        relation_list = create_grammar_relation(sem)
        results.append(f"Question {idx + 1}: {sentences[idx]}\n" + '\n'.join(relation_list))
    path = write_file(2, '\n'.join(results))
    print(f"Grammar relation created successfully. Results are saved at {path}")
    
    # Creating logical form & semantic procedure
    logical_form = [sem.replace(",", " ") for sem in sem_list]
    semantic_procedure = [create_semantic_procedure(tree) for tree in tree_list]
    
    if len(logical_form) != len(semantic_procedure):
        raise ValueError("Length of logical form and semantic procedure must be equal")
    results = []
    for idx, (lf, sp) in enumerate(zip(logical_form, semantic_procedure), 1):
        result = f"Question {idx}: {sentences[idx-1]}\n"
        result += f"Logical form: {lf}\n"
        result += f"Semantic procedure: {sp}\n"
        results.append(result)
    path = write_file(3, '\n'.join(results))
    print(f"Logical form and semantic procedure created successfully. Results are saved at {path}")
    
    # Retrieve answer
    print("Retrieving answer...")
    answer = []
    for procedure in semantic_procedure:
        answer.append(retrive_data(procedure))
    results = []
    for idx, (sentence, ans) in enumerate(zip(sentences, answer), 1):
        result = f"Question {idx}: {sentence}\n"
        result += f"Answer: {ans}\n"
        results.append(result)
    path = write_file(4, '\n'.join(results))
    print(f"Answer retrieved successfully. Results are saved at {path}")
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Assignment 2 NLP')
    parser.add_argument('--grammar_rule_file_name', help="FCFG grammar file name (default is 'grammar.fcfg')", default='grammar.fcfg')
    args = parser.parse_args()
    main(args)
    