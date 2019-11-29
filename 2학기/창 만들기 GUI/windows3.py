import tkinter
class Windows2:
    def __init__(self, parent):
        self.parent = parent
        self.root = tkinter.Toplevel(parent)
        self.root.geometry("400x400")
        button = tkinter.Button(self.root, text="New2", command = self.command2)
        button.pack()

    def command2(self):
        print("sub command")