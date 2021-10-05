import argparse
import os
import json
import spacy
from spacy.gold import GoldParse
from spacy.scorer import Scorer



def main():

    parser = argparse.ArgumentParser(description='A program for evaluation of trainer NER model')

    parser.add_argument("--model_name", help="Specify model name")
    parser.add_argument("--data_string", help="JSON string with training data")
    parser.add_argument("--data_json", help="JSON file with training data")
    

    args = parser.parse_args()    
    
    
    if args.data_string and not args.data_json:
        data = json.loads(args.data_string)        
    else:
        with open(args.data_json, 'r', encoding='utf') as f:
            data = json.loads(f.read())


    model_name = args.model_name            
    if model_name in os.listdir('.'):
        nlp = spacy.load(f'./{model_name}')
        print(f'Model {model_name} loaded\n')
    else:
        print(f'No such model: {model_name}\n')
        return
        
    if "ner" in nlp.pipe_names:
        ner = nlp.get_pipe("ner")
    else:
        print(f"Model {model_name} doesn't have NER pipeline\n")
          
            
    data = list(data.items())            
    scorer = Scorer()
    for input_, annot in data:
        doc_gold_text = nlp.make_doc(input_)
        gold = GoldParse(doc_gold_text, entities=annot['entities'])
        pred_value = nlp(input_)
        scorer.score(pred_value, gold)

    print(scorer.scores['ents_per_type'])
    
    
if __name__ == '__main__':
    main()