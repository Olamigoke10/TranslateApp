import streamlit as st
from googletrans import Translator, LANGUAGES

# Create a dictionary to map language keys to their full names
language_names = {code: name for code, name in LANGUAGES.items()}

def Translate(destination, word):
    try:
        translator = Translator()
        answer = translator.translate(word, src='auto', dest=destination)
    except Exception as e:
        return "An Error Occurred"

    return answer.text

st.title("TRANSLATE APP")

# Get the full language names for display in the selectbox
target_languages = [language_names[code] for code in LANGUAGES.keys()]

# Allow the user to select a target language
select = st.selectbox("Select Target Language", target_languages)

word = st.text_input("Enter the word:")

if st.button("Translate"):
    # Reverse the mapping to get the language code from the full name
    language_code = next(code for code, name in language_names.items() if name == select)
    translated_text = Translate(language_code, word)
    st.write(f"{translated_text}")
