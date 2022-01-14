
import json

import streamlit as st
import requests


def compute_sentence_similarity(text1, text2):
    url = "https://y6wrl4j6v7.execute-api.us-east-1.amazonaws.com/default/SentenceSimilarity"
    payload = json.dumps({'text1': text1, 'text2': text2})
    headers = {'Content-Type': 'application/json'}
    response = requests.request('GET', url, headers=headers, data=payload)
    similarity = json.loads(response.text).get('similarity')
    return similarity


demotext1 = 'NIH funds a lot of great science projects.'
demotext2 = 'A lot of magnificent scientific research projects are funded by NIH.'

st.text('Science Similarity')
st.write('Disclaimer: This is a demonstration. The models used are of public domain, and are not trained with any private or sensitive data such as PII or PHI.')

text1 = st.text_area('Document 1', demotext1)
text2 = st.text_area('Document 2', demotext2)

similarity = compute_sentence_similarity(text1, text2)
st.write('Similarity: {:.4f}'.format(similarity))
