import streamlit as st
from googletrans import Translator, LANGUAGES
from voice import Voice

# Create a dictionary to map language keys to their full names
language_names = {code: name for code, name in LANGUAGES.items()}

def Translate(destination, word):
    try:
        translator = Translator()
        answer = translator.translate(word, src='auto', dest=destination)
    except Exception as e:
        return "An Error Occurred"
    return answer.text

def get_language_code(language_name):
    return next(code for code, name in language_names.items() if name == language_name)

st.title("TRANSLATE APP")

# Get the full language names for display in the selectbox
target_languages = [language_names[code] for code in LANGUAGES.keys()]

# Allow the user to select a target language
select = st.selectbox("Select Target Language", target_languages)

word = st.text_input("Enter the word:")

col1, spacer,  col2 = st.columns([2, 6, 1])

with col1:
    if st.button("Translate"):
        language_code = get_language_code(select)
        translated_text = Translate(language_code, word)
        st.write(f"{translated_text}")

with col2:
    if st.button("Voice"):
        language_code = get_language_code(select)
        translated_text = Translate(language_code, word)
        Voice(translated_text)
