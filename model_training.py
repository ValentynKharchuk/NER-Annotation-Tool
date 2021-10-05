import argparse
import json
import os
import spacy
import random
from spacy.util import minibatch, compounding



def main():

    parser = argparse.ArgumentParser(description='A program for creation and training NER model')

    parser.add_argument("--model_name", help="Specify model name")
    parser.add_argument("--data_string", help="JSON string with training data")
    parser.add_argument("--data_json", help="JSON file with training data")

    args = parser.parse_args()    
    
    model_name = args.model_name
    
    if args.data_string and not args.data_json:
        train_data = json.loads(args.data_string)        
    else:
        with open(args.data_json, 'r', encoding='utf') as f:
            train_data = json.loads(f.read())
                  
    
    for sentence in train_data.keys():
        print(f'Train sample: \n\t{sentence}')
        print('Entities:')
        for entity in train_data[sentence]['entities']:
            print(f'\t{sentence[entity[0]:entity[1]]}, type = {entity[2]}')
        print()
        
    if model_name in os.listdir('.'):
        nlp = spacy.load(f'./{model_name}')
        print(f'Model {model_name} loaded\n')
    else:
        nlp = spacy.blank("uk")
        print(f'Model {model_name} created\n')
        
    if "ner" not in nlp.pipe_names:
        ner = nlp.create_pipe("ner")
        nlp.add_pipe(ner, last=True)
    else:
        ner = nlp.get_pipe("ner")
        
    
    [[ner.add_label(ent[-1]) for ent in train_data[x]['entities']] for x in train_data]
    
    
    n_iter = 50
    
    pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]    
    train_data = list(train_data.items())
        

    optimizer = nlp.begin_training() if model_name not in os.listdir('.') else nlp.resume_training()
           
    with nlp.disable_pipes(*other_pipes):        

        for itn in range(n_iter):

            random.shuffle(train_data)
            losses = {}

            batches = minibatch(train_data, size=compounding(10.0, 32.0, 1.2))
            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(
                    texts,
                    annotations,  
                    drop=0.2,  
                    losses=losses,
                    sgd=optimizer
                )
            print(f"Iteration number: {itn:4}, loss = {losses['ner']:.10f}")
        print()
    
    nlp.to_disk(f"./{model_name}")
    print('Model Saved\n')
    
    
if __name__ == '__main__':
    main()