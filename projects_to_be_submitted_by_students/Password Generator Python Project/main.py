import string
import random
import streamlit as st

def generate_password(length,use_digits,use_special):
    characters=string.ascii_letters
    if use_digits:
        characters+=string.digits
    if use_special:
        characters+=string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))
    
length=st.slider('Set the range for your password',max_value=32,min_value=8)
use_digits=st.checkbox('Include digits')
use_special=st.checkbox('Include special characters')
    
if st.button('Generate'):
    password=generate_password(length,use_digits,use_special)
    st.write(f'Password: `{password}`')