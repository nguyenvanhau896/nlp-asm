# To run this project:
1. Navigate to the Application Directory:
`cd hcmut/nlp/app`
2. Run the Application 
`python main.py`
+ Main entry point: main.py

*Note*: By defult, the application uses `grammar.fcfg` as the grammar file. To specify a different grammar file, use `--grammar_rule_file_name` argument:

`python main.py --grammar_rule_file_name your_grammar.fcfg`

3. View Output: The application generates output files in the `../output/` directory:

+ `p2-q-1.txt` to `p2-q-5.txt`: Contain parsing results, semantic forms, grammar relations, and answers.

### Project structure:

python/

├── hcmut/

│   └── nlp/

│       └── app/

│           ├── data.py

│           ├── file_manager.py

│           ├── grammar.fcfg

│           ├── grammar_relation.py

│           ├── main.py

│           ├── semantic_procedure.py

│       └── output/

│           ├── p2-q-1.txt

│           ├── p2-q-2.txt

│           ├── p2-q-3.txt

│           ├── p2-q-4.txt

│           └── p2-q-5.txt

├── README.md

└── requirements.txt
