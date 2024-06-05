import tkinter as tk
from tkinter import filedialog
import re

def choose_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        label.config(text="Вибраний файл: " + file_path)
        count_text_statistics(file_path)

def count_text_statistics(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    num_sentences = len(re.split(r'[.!?]+', text)) - 1
    num_words = len(re.findall(r'\b\w+\b', text))
    num_letters = len(re.findall(r'\w', text))

    result_text = f"Речень: {num_sentences}\nСлів: {num_words}\nЛітер: {num_letters}"
    result_label.config(text=result_text)

root = tk.Tk()
root.title("Оберіть файл")
# setting window size
width = 400
height = 200
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

label = tk.Label(root, text="")
label.pack(pady=10)

button = tk.Button(root, text="Обрати файл", command=choose_file)
button.pack(pady=5)

result_label = tk.Label(root, text="", justify="left")
result_label.pack(pady=10)

root.mainloop()
