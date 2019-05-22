from tkinter import Tk, scrolledtext, Menu, filedialog, END, messagebox, simpledialog
import os

# root for main window
root = Tk(className=" Untitled - RAPTOR")
textArea = scrolledtext.ScrolledText(root, width=100, height=80)

#
# Functions
#


def new_file():
    # Is there content??
    if len(textArea.get("1.0", END+"-1c")) > 0:
        if messagebox.askyesno("Save??", "Do you wish to save??"):
            save_file()
            textArea.delete("1.0", END)
        else:
            textArea.delete("1.0", END)

    root.title("Untitled - RAPTOR")


def open_file():
    file = filedialog.askopenfile(parent=root, initialdir="/home/DWave", title="Select a text file",
                                  filetypes=(("Text Files", "*.txt"), ("All files", "*.*")))

    root.title(os.path.basename(file.name) + " - RAPTOR")

    if file is not None:
        contents = file.read()
        textArea.insert("1.0", contents)
        file.close()


def find_infile():
    findString = simpledialog.askstring("Find....", "Enter Text")
    textData = textArea.get("1.0", END)

    occurances = textData.upper().count(findString.upper())

    if textData.upper().count(findString.upper()) > 0:
        messagebox.showinfo("Results", findString + " has " + str(occurances) + "occurance(s)")
    else:
        messagebox.showinfo("Results", "No occurances")

    print()


def save_file():
    file = filedialog.asksaveasfile(mode="w", filetypes=(("Text Files", "*.txt"), ("All files", "*.*")))

    if file is not None:
        # slice off the last character from get, as an extra return (enter) is added
        data = textArea.get("1.0", END+"-1c")
        file.write(data)
        file.close()


def about():
    messagebox.showinfo("About", "An alternative to notepad in Python!!!")


def help_dialogue():
    messagebox.showinfo("Help", "This is help")


def exit_root():
    if messagebox.askyesno("Quit", "Are you sure you want to quit??"):
        root.destroy()


# Menu Options
menu = Menu(root)
root.config(menu=menu)
fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New", command=new_file)
fileMenu.add_command(label="Open", command=open_file)
fileMenu.add_command(label="Save", command=save_file)
fileMenu.add_command(label="Find", command=find_infile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exit_root)

helpMenu = Menu(menu)
menu.add_command(label="Help", command=help_dialogue)
menu.add_command(label="About", command=about)

textArea.pack()

# Keep window up
root.mainloop()
