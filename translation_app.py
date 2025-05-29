from tkinter import *
from tkinter import ttk
from googletrans import Translator


translator = Translator()

async def translate_text():
    text_to_translate = input_text.get("1.0", END).strip()
    target_lang = lang_combobox.get()
    
    if not text_to_translate:
        output_text.delete(1.0, END)
        output_text.insert(END, "Please enter text to translate")
        return
    
    try:
        translated = await translator.translate(text_to_translate, dest=target_lang)
        output_text.delete(1.0, END)
        output_text.insert(END, translated.text)
    except Exception as e:
        output_text.delete(1.0, END)
        output_text.insert(END, f"Error: {str(e)}")

root = Tk()
root.title("Language Translator")
root.geometry("600x400")

input_label = Label(root, text="Enter text to translate:")
input_label.pack(pady=5)
input_text = Text(root, height=5, width=70)
input_text.pack(pady=5)

lang_label = Label(root, text="Select target language:")
lang_label.pack(pady=5)
lang_combobox = ttk.Combobox(root, values=[
    'en', 'es', 'fr', 'de', 'it', 'ja', 'ko', 'zh-cn', 'hi'
], width=10)
lang_combobox.set('en')
lang_combobox.pack(pady=5)

translate_btn = Button(root, text="Translate", command=translate_text)
translate_btn.pack(pady=10)

output_label = Label(root, text="Translated text:")
output_label.pack(pady=5)
output_text = Text(root, height=5, width=70)
output_text.pack(pady=5)

root.mainloop()