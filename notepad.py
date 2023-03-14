
import tkinter as tk
from tkinter import filedialog, colorchooser

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title('Text Editor')

        # Create menu bar
        menubar = tk.Menu(self.root)

        # File menu
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='New', command=self.new_file)
        filemenu.add_command(label='Open', command=self.open_file)
        filemenu.add_command(label='Save', command=self.save_file)
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=self.root.quit)
        menubar.add_cascade(label='File', menu=filemenu)

        # Edit menu
        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label='Cut', command=self.cut)
        editmenu.add_command(label='Copy', command=self.copy)
        editmenu.add_command(label='Paste', command=self.paste)
        menubar.add_cascade(label='Edit', menu=editmenu)

        # View menu
        viewmenu = tk.Menu(menubar, tearoff=0)
        viewmenu.add_command(label='Change background color', command=self.change_bg_color)
        viewmenu.add_command(label='Change text color', command=self.change_text_color)
        menubar.add_cascade(label='View', menu=viewmenu)

        self.root.config(menu=menubar)

        # Create text widget
        self.text = tk.Text(self.root)
        self.text.pack(fill='both', expand=True)

    def new_file(self):
        self.text.delete('1.0', 'end')

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
        if file_path:
            with open(file_path, 'r') as f:
                self.text.delete('1.0', 'end')
                self.text.insert('1.0', f.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension='.txt')
        if file_path:
            with open(file_path, 'w') as f:
                f.write(self.text.get('1.0', 'end'))

    def cut(self):
        self.text.event_generate('<<Cut>>')

    def copy(self):
        self.text.event_generate('<<Copy>>')

    def paste(self):
        self.text.event_generate('<<Paste>>')

    def change_bg_color(self):
        color = colorchooser.askcolor(title='Select background color')
        if color:
            self.text.config(bg=color[1])

    def change_text_color(self):
        color = colorchooser.askcolor(title='Select text color')
        if color:
            self.text.config(fg=color[1])

if __name__ == '__main__':
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()

