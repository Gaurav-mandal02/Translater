from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

# Function to translate text
def change(text='type', src='English', dest='Hindi'):
    try:
        # Convert language names to codes
        src_code = [k for k, v in LANGUAGES.items() if v.lower() == src.lower()][0]
        dest_code = [k for k, v in LANGUAGES.items() if v.lower() == dest.lower()][0]

        # Perform translation
        translator = Translator()
        translated = translator.translate(text, src=src_code, dest=dest_code)
        return translated.text
    except Exception as e:
        messagebox.showerror("Translation Error", f"Error: {e}")
        return ""

# Function to handle translation process
def data():
    src_lang = comb_sor.get()
    dest_lang = comb_dest.get()
    msg = sor_txt.get(1.0, END).strip()  # Get source text

    if not msg:
        messagebox.showwarning("Input Error", "Source text is empty!")
        return

    translated_text = change(text=msg, src=src_lang, dest=dest_lang)
    if translated_text:
        des_txt.delete(1.0, END)
        des_txt.insert(END, translated_text)

# Main Application Window
root = Tk()
root.title('Translator')
root.geometry('500x700')
root.config(bg='yellow')

# Title Label
Label(root, text='Translator', font=('Times New Roman', 40, 'bold'), bg='red').pack(pady=10)

# Source Text Label and Textbox
Label(root, text='Source Text', font=('Times New Roman', 20, 'bold'), bg='yellow').place(x=10, y=80)
sor_txt = Text(root, font=('Times New Roman', 15), wrap=WORD, bg='sky blue')
sor_txt.place(x=10, y=120, height=150, width=480)

# Language Selection Comboboxes
list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(root, value=list_text, font=('Times New Roman', 12))
comb_sor.place(x=10, y=300, height=40, width=200)
comb_sor.set('English')

comb_dest = ttk.Combobox(root, value=list_text, font=('Times New Roman', 12))
comb_dest.place(x=280, y=300, height=40, width=200)
comb_dest.set('Hindi')

# Translate Button
Button(root, text='Translate', font=('Times New Roman', 15), relief=RAISED, command=data, bg='red').place(x=190, y=360, height=40, width=120)

# Destination Text Label and Textbox
Label(root, text='Destination Text', font=('Times New Roman', 20, 'bold'), bg='yellow').place(x=10, y=420)
des_txt = Text(root, font=('Times New Roman', 15), wrap=WORD, bg='sky blue')
des_txt.place(x=10, y=460, height=150, width=480)

# Run the main loop
root.mainloop()
