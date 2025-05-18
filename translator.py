from googletrans import Translator

def translate_text(text, src='en', dest='hi'):
    translator = Translator()
    try:
        translated = translator.translate(text, src=src, dest=dest)
        return translated.text
    except Exception as e:
        return f"Error: {str(e)}"