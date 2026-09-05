import requests
import os
import json
import pandas as pd
import joblib

def create_embedding(text):
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text
    })
    emedding = r.json()['embeddings']
    return emedding

jsons = os.listdir("newjsons")
my_dicts = []
chunk_id = 0
for json_file in jsons:
    with open(f"newjsons/{json_file}") as f:
        content = json.load(f)
    print(f"Creating Embeddings for {json_file}")
    
    embeddings = create_embedding([c['text'] for c in content['chunks']])
    for i,chunk in enumerate(content['chunks']):
        chunk['chunk_id'] = chunk_id
        chunk['embedding'] = embeddings[i]
        chunk_id += 1
        my_dicts.append(chunk)

df = pd.DataFrame.from_records(my_dicts)
joblib.dump(df,'embeddings.joblib')