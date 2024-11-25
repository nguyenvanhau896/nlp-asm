# grammar_relation.py
from data import *
from collections import deque

class Relation:
    def __init__(self, left, right, type):
        self.left = left
        self.right = right
        self.type = type
    
    def __str__(self) -> str:
        return f"({self.left} {self.type} {self.right})"

agent_list = ["EM", "ANH"]
pred_list = ["TRAVEL1", "TRAVEL2", "REMIND1"] # define verb that can be predicate
query_list = ["LIST1", "WHICH1", "WHAT1", "HOW1", "HOW2"] # define query

def create_grammar_relation(sem):
    # Create grammar relation from semantic representation
    sem = sem.replace("(", " ").replace(")", " ").replace(",", " ").replace("'","").split()
    relation_list = []
    
    for idx, token in enumerate(sem):
        if token in agent_list:
            relation_list.append(str(Relation("s1", SEM_MAPPING[token], "AGENT")))
        elif token in pred_list:
            relation_list.append(str(Relation("s1", SEM_MAPPING[token], "PRED")))
        elif token in query_list:
            relation_list.append(str(Relation("s1", SEM_MAPPING[token], "QUERY")))
        elif token in ["DEST", "SOURCE"]:
            relation_list.append(str(Relation("s1", f"({sem[idx+1]} {sem[idx+2]} {SEM_MAPPING[sem[idx+3]]})", token)))
    
    return relation_list
            
