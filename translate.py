from googletrans import Translator, LANGUAGES

# Print the available language codes in a more readable format
print("Available language codes:")
print(", ".join(LANGUAGES.keys()))

# Create a Translator object
translator = Translator()

# Input from user
user_word = input("Enter the text to translate: ")
language = input("Enter language to translate to (e.g., 'en' for English): ")

try:
    if language in LANGUAGES.keys():
        answer = translator.translate(user_word, src='en', dest=language)
        if answer.src == answer.dest:
            print("Same language")
        else:
            print(answer.text)
    else:
        print("Invalid language code.")
except Exception as e:
    print(f"An error occurred: {e}")
