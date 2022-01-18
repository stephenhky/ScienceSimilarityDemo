
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


# Presentation details
st.header('Science Similarity Detection')
col1, col2 = st.columns((2, 1))
col1.text('Goal: Automate the process of identifying and withdrawing duplicated or overlapping grant applications.')
col1.text('Achievement and Impact:')
col1.text('- Reduces ~95% of the workload.')
col1.text('- Processes 18k-23k~ grant applications bi-monthly.')
col1.text('- Manually verified 99.9% accuracy.')
col1.text('- Picks up similar sciences missed by human review.')
col2.image('histscisim.png')

# demonstration
demotext1 = 'NIH funds a lot of great science projects.'
demotext2 = 'A lot of magnificent scientific research projects are funded by NIH.'

st.header('Demonstration')
st.write('Disclaimer: This is a demonstration. The models used are of public domain, and are not trained with any private or sensitive data such as PII or PHI.')

text1 = st.text_area('Document 1', demotext1)
text2 = st.text_area('Document 2', demotext2)

similarity = compute_sentence_similarity(text1, text2)
st.write('Similarity: {:.4f}'.format(similarity))
