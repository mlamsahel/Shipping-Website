import tkinter as gui

savedString = None
current_window = None  # To keep track of the current open window

def createGUI():
    global source
    source = gui.Tk()
    source.title("Amazon't Database")
    source.geometry("1000x800")

    create_button("Add Customer")
    create_button("Add Distributor")
    create_button("Add Order")
    create_button("Add Product")
    create_button("Add Purchase")

    source.mainloop()

def create_button(text):
    button = gui.Button(source, text=text, command=lambda t=text: open_window(t))
    button.pack()

def open_window(button_text):
    global current_window

    if current_window is not None and current_window.winfo_exists():
        current_window.destroy()

    current_window = gui.Toplevel()
    current_window.title(button_text)
    current_window.geometry("300x150")

# Run the GUI
createGUI()
