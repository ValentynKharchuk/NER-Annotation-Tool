import argparse
import os
import spacy



def main():

    parser = argparse.ArgumentParser(description='A program for prediction NER entities in text using trained model')

    parser.add_argument("--model_name", help="Specify model name")
    parser.add_argument("--data_string", help="String with data for predicting")
    parser.add_argument("--data_file", help="File with data for predicting")

    args = parser.parse_args()    
    
    model_name = args.model_name
    
    if args.data_string and not args.data_file:
        data = args.data_string
    else:
        with open(args.data_file, 'r', encoding='utf') as f:
            data = f.read()
                                          
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
                        
    doc = nlp(data)
    
    
    print(f'Input text:\n{data}')
    print("Tokens", [(t.text, t.ent_type_) for t in doc])
    print("Entities", [(ent.text, ent.label_) for ent in doc.ents])

    
    
if __name__ == '__main__':
    main()