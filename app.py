
import json

import numpy as np
from scipy.spatial.distance import cosine
import streamlit as st
from sentence_transformers import SentenceTransformer

demotext1 = 'NIH funds a lot of great science projects.'
demotext2 = 'A lot of magnificent scientific research projects are funded by NIH.'

smodel = SentenceTransformer('allenai-specter')

st.text('Science Similarity')
st.write('Disclaimer: This is a demonstration. The models used are of public domain, and are not trained with any private or sensitive data such as PII or PHI.')

text1 = st.text_area('Document 1', demotext1)
text2 = st.text_area('Document 2', demotext2)

vec1 = smodel.encode(text1)
vec2 = smodel.encode(text2)

similarity = 1 - cosine(vec1, vec2)
st.write('Similarity: {:.4f}'.format(similarity))
