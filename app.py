import streamlit as st
from translator import translate_text

st.title("🌐 Language Translation Tool")

text_input = st.text_area("Enter text to translate:")
source_lang = st.selectbox("Source Language", ['en', 'hi', 'es', 'fr', 'de', 'zh-cn'])
target_lang = st.selectbox("Target Language", ['hi', 'en', 'es', 'fr', 'de', 'zh-cn'])

if st.button("Translate"):
    if text_input.strip() == "":
        st.warning("Please enter some text to translate.")
    else:
        result = translate_text(text_input, src=source_lang, dest=target_lang)
        st.success(result)