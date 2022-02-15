
import json

import streamlit as st
import requests


def compute_sentence_similarity(text1, text2, sbertmodel):
    url = "https://y6wrl4j6v7.execute-api.us-east-1.amazonaws.com/default/SentenceSimilarity"
    payload = json.dumps({'text1': text1, 'text2': text2, 'sbertmodel': sbertmodel})
    headers = {'Content-Type': 'application/json'}
    response = requests.request('GET', url, headers=headers, data=payload)
    similarity = json.loads(response.text).get('similarity')
    return similarity


# Presentation details
st.header('Science Similarity Detection')

# demonstration
demotext1 = 'Quantum field theory can be dealt with using either canonical quantization or path integrals.'
demotext2 = 'There are two approaches in quantum field theory, namely, canonical quantization and path integrals.'
available_sentence_bert_models = [
    'allenai-specter',
    'scibert-nli'
    'biobert-nli'
]

st.header('Demonstration')
st.write('Disclaimer: This is a demonstration. The models used are of public domain, and are not trained with any private or sensitive data such as PII or PHI.')

text1 = st.text_area('Document 1', demotext1)
text2 = st.text_area('Document 2', demotext2)

sbert_model = st.selectbox(
    'Sentence-BERT Model',
    available_sentence_bert_models
)

if st.button('Compute Similarity!'):
    similarity = compute_sentence_similarity(text1, text2)
    st.write('Similarity: {:.4f}'.format(similarity))
