import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.font import Font

def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return
    
    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)

    window.title(f"Open File: {filepath}")

def save_file(window, text_edit):
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return
    
    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    window.title(f"Save File: {filepath}")

def change_font_size(text_edit, font, delta):
    size = font['size']
    new_size = size + delta
    if new_size > 0:  # Prevent the font size from becoming zero or negative
        font.configure(size=new_size)

def apply_bold(text_edit):
    current_tags = text_edit.tag_names("sel.first")
    if "bold" in current_tags:
        text_edit.tag_remove("bold", "sel.first", "sel.last")
    else:
        text_edit.tag_add("bold", "sel.first", "sel.last")

def apply_highlight(text_edit, color):
    text_edit.tag_add("highlight", "sel.first", "sel.last")
    text_edit.tag_configure("highlight", background=color)

def apply_color(text_edit, color):
    text_edit.tag_add("color", "sel.first", "sel.last")
    text_edit.tag_configure("color", foreground=color)

def main():
    window = tk.Tk()
    window.title("Text Editor")
    window.rowconfigure(0, minsize=40)  # Adjust minsize as needed for the buttons to fit
    window.rowconfigure(1, minsize=400)  # Adjust remaining space for the text widget
    window.columnconfigure(0, minsize=600)

    # Font
    font = Font(family="Arial", size=14)

    # Text widget
    text_edit = tk.Text(window, font=font, wrap="word")
    text_edit.grid(row=1, column=0, sticky="nsew")

    # Frame
    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    frame.grid(row=0, column=0, sticky="ew")  # Set frame at the top row spanning entire width

    # Scrollbar
    scrollbar = tk.Scrollbar(window, orient="vertical", command=text_edit.yview)
    scrollbar.grid(row=1, column=1, sticky="ns")
    text_edit['yscrollcommand'] = scrollbar.set

    # Buttons
    save_button = tk.Button(frame, text="Save", command=lambda: save_file(window, text_edit))
    open_button = tk.Button(frame, text="Open", command=lambda: open_file(window, text_edit))
    increase_font_button = tk.Button(frame, text="+", command=lambda: change_font_size(text_edit, font, 1))
    decrease_font_button = tk.Button(frame, text="-", command=lambda: change_font_size(text_edit, font, -1))
    bold_button = tk.Button(frame, text="Bold", command=lambda: apply_bold(text_edit))
    highlight_button = tk.Button(frame, text="Highlight", command=lambda: apply_highlight(text_edit, "yellow"))
    color_button = tk.Button(frame, text="Color", command=lambda: apply_color(text_edit, "red"))

    save_button.pack(side=tk.LEFT, padx=5, pady=5)
    open_button.pack(side=tk.LEFT, padx=5)
    increase_font_button.pack(side=tk.LEFT, padx=5)
    decrease_font_button.pack(side=tk.LEFT, padx=5)
    bold_button.pack(side=tk.LEFT, padx=5)
    highlight_button.pack(side=tk.LEFT, padx=5)
    color_button.pack(side=tk.LEFT, padx=5)

    # Configure bold tag
    text_edit.tag_configure("bold", font=Font(family="Arial", size=14, weight="bold"))

    window.mainloop()

main()
